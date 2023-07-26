import re
import os
import openai
import openai.error
from dotenv import load_dotenv
from ...typing import sha256, Dict, get_type_hints

load_dotenv()
openai.api_key = '28MJ7F_t5nxPj9dgyGUJXj8Yb1L4Y1ZdxCU06CVa5Uw'
openai.api_base = "https://chimeragpt.adventblocks.cc/api/v1"

url = 'https://chimeragpt.adventblocks.cc/'
model = [
    'gpt-3.5-turbo',
    'gpt-3.5-turbo-0301',
    'gpt-3.5-turbo-poe',
    'gpt-3.5-turbo-16k',
    'gpt-3.5-turbo-16k-poe',
    'gpt-4',
    'gpt-4-0314',
    'gpt-4-poe',
    'gpt-4-32k',
    'gpt-4-32k-poe',
    'claude-instant',
    'claude-instant-100k',
    'claude-2-100k',
    'chat-bison-001',
    'sage',
    'llama-2-7b-chat',
    'llama-2-13b-chat',
    'llama-2-70b-chat',
    'kandinsky'
]

supports_stream = True
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    try:
        if model == 'kandinsky':
            response = openai.Image.create(prompt=messages[-1]['content'],n=1,size="1024x1024")
            try:
                yield '![]('+response["data"][0]["url"]+')'
            except:
                yield 'Image generation error. This may be because your image is illegal or our service has malfunctioned.'
        else:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                stream=stream
            )
            if stream:
                for chunk in response:
                    yield chunk.choices[0].delta.get("content", "")
            else:
                yield response.choices[0]['message'].get("content", "")
            
    except openai.error.APIError as e:
        if e.http_status == 429:
            detail_pattern = re.compile(r'{"detail":"(.*?)"}')
            match = detail_pattern.search(e.user_message)
            if match:
                error_message = match.group(1)
                print(error_message)
                yield error_message
            else:
                print(e.user_message)
                yield e.user_message
        else:
            raise


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
