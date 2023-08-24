import os
import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://chat.zhulei.xyz/'
model = ['gpt-3.5-turbo']
supports_stream = True
needs_auth = False
working = False

headers = {
    'Origin':'https://chat.zhulei.xyz',
    'Referer':'https://chat.zhulei.xyz/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Content-Type':'text/plain;charset=UTF-8',
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    json_data = {
  "messages": messages,
  "temperature": kwargs.get("temperature", 0.6),
  "password": "",
  "model": "gpt-3.5-turbo"
    }
    r = requests.post('https://chat.zhulei.xyz/api',json=json_data,headers=headers,stream=True)
    for chunk in r.iter_content(chunk_size=2048):
        if chunk:
            yield chunk.decode('utf-8',errors='ignore')

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])