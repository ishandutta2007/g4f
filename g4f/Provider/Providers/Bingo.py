import requests
import uuid
import json
import re
import os
from ...typing import sha256, Dict, get_type_hints

url = 'https://bing2.lemonsoftware.eu.org/'
model = ['gpt-4','bing']
supports_stream = True
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    bing_cookie = str(uuid.uuid4())
    create = requests.post('https://hf4all-bingo.hf.space/api/create',
                        headers={
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
                            'Cookie':'BING_COOKIE='+bing_cookie+'; BING_UA=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F115.0.0.0%20Safari%2F537.36%20Edg%2F115.0.1901.183; BING_IP=11.105.176.100'
                        })
    try:
        conversationId = create.json().get('conversationId')
        clientId = create.json().get('clientId')
        conversationSignature = create.json().get('conversationSignature')
    except:
        create = requests.post('https://hf4all-bingo.hf.space/api/create',
                        headers={
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
                            'Cookie':'BING_COOKIE='+bing_cookie+'; BING_UA=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F115.0.0.0%20Safari%2F537.36%20Edg%2F115.0.1901.183; BING_IP=11.105.176.100'
                        })
        conversationId = create.json().get('conversationId')
        clientId = create.json().get('clientId')
        conversationSignature = create.json().get('conversationSignature')
    payload = {
        "conversationId": conversationId,
        "conversationSignature": conversationSignature,
        "clientId": clientId,
        "invocationId": 0,
        "conversationStyle": "Creative",
        "prompt": messages[-1]['content']
    }
    sydney = requests.post('https://hf4all-bingo.hf.space/api/sydney',data=json.dumps(payload),stream=True,headers={
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
                            'Content-Type':'application/json',
                            'Cookie':'BING_COOKIE='+bing_cookie+'; BING_UA=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F115.0.0.0%20Safari%2F537.36%20Edg%2F115.0.1901.183; BING_IP=11.105.176.100'
                        })
    lasttoken = ''
    for line in sydney.text.split(''):
        try:
            if line:
                try:
                    line_ = json.loads(line)['arguments'][0]['messages'][0]['text'][len(lasttoken):]
                    lasttoken = json.loads(line)['arguments'][0]['messages'][0]['text']
                    if 'Searching the web for:' not in line_ :
                        yield line_
                except:
                    pass
                    '''
                    for text in json.loads(line)['items']['messages']:
                        yield text['text'] 
                    '''
        except:
            pass

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])