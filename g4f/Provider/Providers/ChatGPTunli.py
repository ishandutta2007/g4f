import os
import requests,json
from ...typing import sha256, Dict, get_type_hints

url = 'https://www.chatgptunli.com/chatgpt/'
model = ['gpt-3.5-turbo']
supports_stream = True
needs_auth = False
working = True

headers = {
    'Origin':'https://www.chatgptunli.com',
    'Referer':'https://www.chatgptunli.com/chatgpt/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Content-Type':'application/json',
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    json_data = {
  "id": "default",
  "botId": "default",
  "session": "N/A",
  "clientId": "wc6c7y0t45",
  "contextId": 382,
  "messages": messages,
  "newMessage": messages[-1]['content'],
  "stream": True
    }
    r = requests.post('https://www.chatgptunli.com/wp-json/mwai-ui/v1/chats/submit',json=json_data,headers=headers,stream=True)
    for chunk in r.iter_lines():
        if chunk and chunk.startswith(b'data:'):
            data = json.loads(chunk.decode()[5:])
            if data['type'] == 'live':
                yield data['data']

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])