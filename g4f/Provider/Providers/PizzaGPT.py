import os
from curl_cffi import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://pizzagpt.it/'
model = ['gpt-3.5-turbo']
supports_stream = False
needs_auth = False
working = True

headers = {
    'Origin':'https://pizzagpt.it',
    'Referer':'https://pizzagpt.it/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Secret':'Marinara',
    'Content-Type':'text/plain;charset=UTF-8',
    'Cookie':'dntd=false; cf_clearance=r4xzN9B6NS2nW5gq2Q1YOgiYw1zu3xs81FmZyNjSVBg-1690797483-0-0.2.1690797483; n-req=1'
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    conversation = 'This is a conversation between a human and a language model. The language model should always respond as the assistant, referring to the past history of messages if needed.\n'
    
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    
    conversation += 'assistant: '
    json_data = {
        "question": conversation
    }
    r = requests.post('https://pizzagpt.it/api/chat-completion',json=json_data,headers=headers,impersonate='chrome110')
    yield r.json()['answer']['content']

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])