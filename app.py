import os
import time
import json
import random
import requests
import g4f
from fastapi import FastAPI,Response, status
from typing import Dict, NewType, Union, Optional, List, get_type_hints
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse,JSONResponse
from fastapi.openapi.utils import get_openapi
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel



#app = FastAPI(docs_url=None, redoc_url=None)
app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

class chat_completions_Item(BaseModel):
  stream : bool = False
  model : str = 'gpt-3.5-turbo'
  messages : list = [{'role': 'user', 'content':"Say 'Hello World'."}]
  provider: Union[str, None] = None
  temperature : float = 0.8
  presence_penalty: float = 0
  frequency_penalty: float = 0
  top_p: float = 1

class completions_Item(BaseModel):
  stream : bool = False
  model : str = 'gpt-3.5-turbo'
  prompt : str = "Say 'Hello World'."
  provider : Union[str, None] = None
  temperature : float = 0.8
  presence_penalty: float = 0
  frequency_penalty: float = 0
  top_p: float = 1

def auto_select(model:str='gpt-3.5-turbo',stream:bool=False):
  r = requests.get('https://gpt.lemonsoftware.eu.org/v1/status')
  data = r.json()['data']
  model_providers = set()
  random.shuffle(data)
  for provider_info in data:
    for model_info in provider_info['model']:
        if model in model_info:
          model_providers.add(provider_info['provider'])
          if model_info[model]['status'] == 'Active':
            if stream == True and getattr(g4f.Provider,provider_info['provider']).supports_stream == False:
              continue
            return [getattr(g4f.Provider,provider_info['provider']),provider_info['provider']]
    else:
        continue
    break
  if not model_providers:
    return None
  active_providers = set()
  for provider_info in data:
    for model_info in provider_info['model']:
      for model in model_info.values():
        if model['status'] == 'Active':
          if stream == True and getattr(g4f.Provider,provider_info['provider']).supports_stream == False:
              continue
          active_providers.add(provider_info['provider'])
  chooseable_providers = model_providers & active_providers
  if not chooseable_providers:
    return None
  chooseable_provider = random.choice(list(chooseable_providers))
  return [getattr(g4f.Provider,chooseable_provider),chooseable_provider]

@app.post("/v1/chat/completions")
def chat_completions(item: chat_completions_Item,responses: Response):
  stream = item.stream
  model = item.model.lower()
  messages = item.messages
  provider_name = item.provider
  temperature = item.temperature
  presence_penalty = item.presence_penalty
  frequency_penalty = item.frequency_penalty
  top_p = item.top_p

  if provider_name:
    try:
      response = g4f.ChatCompletion.create(model=model, provider=getattr(g4f.Provider,provider_name),stream=stream,messages=messages,temperature=temperature,presence_penalty=presence_penalty,frequency_penalty=frequency_penalty,top_p=top_p)
    except:
      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "There was an error","type": "invalid_request_error","param": None,"code": 500}})
  else:
    provider = auto_select(model=model,stream=stream)
    if provider == None:
      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "The model is invalid or not working.","type": "invalid_request_error","param": None,"code": 500}})
    if stream and provider[0].supports_stream == False:
      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "Stream is not supported.","type": "invalid_request_error","param": None,"code": 500}})
    provider_name = provider[1]
    try:
      response = g4f.ChatCompletion.create(model=model, provider=provider[0],stream=stream,messages=messages,temperature=temperature,presence_penalty=presence_penalty,frequency_penalty=frequency_penalty,top_p=top_p)
    except:
      provider = auto_select(model=model,stream=stream)
      if provider == None:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "The model is invalid or not working.","type": "invalid_request_error","param": None,"code": 500}})
      if stream and provider[0].supports_stream == False:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "Stream is not supported.","type": "invalid_request_error","param": None,"code": 500}})
      provider_name = provider[1]
      try:
        response = g4f.ChatCompletion.create(model=model, provider=provider[0],stream=stream,messages=messages,temperature=temperature,presence_penalty=presence_penalty,frequency_penalty=frequency_penalty,top_p=top_p)
      except:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "There was an error.Please try again.","type": "server_error","param": None,"code": 500}})
  
  
  if not stream:
    completion_timestamp = int(time.time())
    completion_id = ''.join(random.choices(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=28))
    return {
        'id': 'chatcmpl-%s' % completion_id,
        'object': 'chat.completion',
        'created': completion_timestamp,
        'model': model,
        'provider':provider_name,
        'usage': {
            'prompt_tokens': len(messages),
            'completion_tokens': len(response),
            'total_tokens': len(messages)+len(response)
        },
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': response
            },
            'finish_reason': 'stop',
            'index': 0
        }]
    }
  
  def stream():
    nonlocal response
    for token in response:
      completion_timestamp = int(time.time())
      completion_id = ''.join(random.choices(
          'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=28))
      completion_data = {
        'id': f'chatcmpl-{completion_id}',
        'object': 'chat.completion.chunk',
        'created': completion_timestamp,
        'model': model,
        'provider':provider_name,
        'choices': [
            {
              'delta': {
                  'content': token
              },
              'index': 0,
              'finish_reason': None
            }
        ]
      }
      yield 'data: %s\n\n' % json.dumps(completion_data, separators=(',' ':'))
      time.sleep(0.1)
  return StreamingResponse(stream(), media_type='text/event-stream')

@app.post("/v1/completions")
def completions(item: completions_Item,responses: Response):
  stream = item.stream
  model = item.model.lower()
  messages = [{'role': 'user', 'content':item.prompt}]
  provider_name = item.provider
  temperature = item.temperature
  presence_penalty = item.presence_penalty
  frequency_penalty = item.frequency_penalty
  top_p = item.top_p
  if provider_name:
    try:
      response = g4f.ChatCompletion.create(model=model, provider=getattr(g4f.Provider,provider_name),stream=stream,messages=messages,temperature=temperature,presence_penalty=presence_penalty,frequency_penalty=frequency_penalty,top_p=top_p)
    except:
      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "There was an error.","type": "invalid_request_error","param": None,"code": 500}})

  else:
    provider = auto_select(model=model,stream=stream)
    if provider == None:
      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "The model is invalid or not working.","type": "invalid_request_error","param": None,"code": 500}})
    if stream and provider[0].supports_stream == False:
      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "Stream is not supported.","type": "invalid_request_error","param": None,"code": 500}})
    provider_name = provider[1]
    try:
      response = g4f.ChatCompletion.create(model=model, provider=provider[0],stream=stream,messages=messages,temperature=temperature,presence_penalty=presence_penalty,frequency_penalty=frequency_penalty,top_p=top_p)
    except:
      provider = auto_select(model=model,stream=stream)
      if provider == None:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "The model is invalid or not working.","type": "invalid_request_error","param": None,"code": 500}})
      if stream and provider[0].supports_stream == False:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "Stream is not supported.","type": "invalid_request_error","param": None,"code": 500}})
      provider_name = provider[1]
      try:
        response = g4f.ChatCompletion.create(model=model, provider=provider[0],stream=stream,messages=messages,temperature=temperature,presence_penalty=presence_penalty,frequency_penalty=frequency_penalty,top_p=top_p)
      except:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": {"message": "There was an error.Please try again.","type": "server_error","param": None,"code": 500}})
    
  if not stream:
    completion_timestamp = int(time.time())
    completion_id = ''.join(random.choices(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=28))
    return {
        'id': 'cmpl-%s' % completion_id,
        'object': 'text.completion',
        'created': completion_timestamp,
        'model': model,
        'provider':provider_name,
        'usage': {
            'prompt_tokens': len(messages),
            'completion_tokens': len(response),
            'total_tokens': len(messages)+len(response)
        },
        'choices': [{
                'text': response,
                'finish_reason': 'length',
                "logprobs": None,
                'index': 0
        }]
    }
  
  def stream():
    nonlocal response
    for token in response:
      completion_timestamp = int(time.time())
      completion_id = ''.join(random.choices(
          'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=28))
      completion_data = {
        'id': f'cmpl-{completion_id}',
        'object': 'text.completion.chunk',
        'created': completion_timestamp,
        'model': model,
        'provider':provider_name,
        'choices': [
            {
              'delta': {
                  'text': token
              },
              'index': 0,
              'finish_reason': None
            }
        ]
      }
      yield 'data: %s\n\n' % json.dumps(completion_data, separators=(',' ':'))
      time.sleep(0.1)
  return StreamingResponse(stream(), media_type='text/event-stream')

@app.get("/v1/dashboard/billing/subscription")
@app.get("/dashboard/billing/subscription")
async def billing_subscription():
  return {
  "object": "billing_subscription",
  "has_payment_method": True,
  "canceled": False,
  "canceled_at": None,
  "delinquent": None,
  "access_until": 2556028800,
  "soft_limit": 6944500,
  "hard_limit": 166666666,
  "system_hard_limit": 166666666,
  "soft_limit_usd": 416.67,
  "hard_limit_usd": 9999.99996,
  "system_hard_limit_usd": 9999.99996,
  "plan": {
    "title": "Pay-as-you-go",
    "id": "payg"
  },
  "primary": True,
  "account_name": "OpenAI",
  "po_number": None,
  "billing_email": None,
  "tax_ids": None,
  "billing_address": {
    "city": "New York",
    "line1": "OpenAI",
    "country": "US",
    "postal_code": "NY10031"
  },
  "business_address": None
}


@app.get("/v1/dashboard/billing/usage")
@app.get("/dashboard/billing/usage")
async def billing_usage(start_date:str='2023-01-01',end_date:str='2023-01-31'):
  return {
  "object": "list",
  "daily_costs": [
    {
      "timestamp": time.time(),
      "line_items": [
        {
          "name": "GPT-4",
          "cost": 0.0
        },
        {
          "name": "Chat models",
          "cost": 1.01
        },
        {
          "name": "InstructGPT",
          "cost": 0.0
        },
        {
          "name": "Fine-tuning models",
          "cost": 0.0
        },
        {
          "name": "Embedding models",
          "cost": 0.0
        },
        {
          "name": "Image models",
          "cost": 16.0
        },
        {
          "name": "Audio models",
          "cost": 0.0
        }
      ]
    }
  ],
  "total_usage": 1.01
}

@app.get("/v1/models")
def models():
  import g4f.models
  model = {"data":[]}
  for i in g4f.models.ModelUtils.convert:
    model['data'].append({
            "id": i,
            "object": "model",
            "owned_by": g4f.models.ModelUtils.convert[i].base_provider,
            "tokens": 99999,
            "fallbacks": None,
            "endpoints": [
                "/v1/chat/completions"
            ],
            "limits": None,
            "permission": []
        })
  return model

@app.get("/v1/providers")
async def providers():
  files = os.listdir("g4f/Provider/Providers")
  files = [f for f in files if os.path.isfile(os.path.join("g4f/Provider/Providers", f))]
  files.sort(key=str.lower)
  providers_data = {"data":[]}
  for file in files:
    if file.endswith(".py"):
      name = file[:-3]
      try:
          p = getattr(g4f.Provider,name)
          providers_data["data"].append({
          "provider": str(name),
          "model": list(p.model),
          "url": str(p.url),
          "working": bool(p.working),
          "supports_stream": bool(p.supports_stream)
          })
      except:
            pass
  return providers_data

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="GPT API",
        version="1.0.0",
        summary="GPT API",
        description="[Try Online](https://chatgpt-next-web.lemonsoftware.eu.org/)",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://gpt-status.lemonsoftware.eu.org/icon.svg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi

@app.exception_handler(StarletteHTTPException)

async def custom_http_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": {"message": "Invalid URL","type": "invalid_request_error","param": None,"code": 404}})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)