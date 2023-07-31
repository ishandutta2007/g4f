import os
import requests

from ...typing import sha256, Dict, get_type_hints
url = 'https://1.b88.asia/'
models = {
  "gpt-3.5-turbo": "chinchilla",
  "claude-instant-100k":"a2_100k",
  "claude-instant":"a2",
  "claude-2-100k":"a2_2", 
  "palm2":"acouchy"
}
model = models.keys()
supports_stream = True
needs_auth = False
working = True

headers = {
        'Content-Type':'application/json',
        'origin': 'https://1.b88.asia',
        'referer': 'https://1.b88.asia/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    conversation = '这是一个人和一个语言模型之间的对话。语言模型应该始终作为助理进行响应，如果需要，可以参考过去的消息历史。\n'
    for message in messages:
        conversation += '%s：%s\n' % (message['role'], message['content'])
    conversation += '助理: '
    json_data = {
        "prompt": conversation,
        "options": {},
        "systemMessage": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
        "temperature": kwargs.get("temperature", 0.8),
        "top_p": kwargs.get("top_p", 1),
        "model": models[model],
        "user": None
    }
    response = requests.post('https://1.b88.asia/api/chat-process', headers=headers, json=json_data, stream=True)
    response.encoding = 'utf-8'
    for token in response.iter_content(chunk_size=2048):
        if token:
            yield token.decode('utf-8',errors='ignore')
            

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])