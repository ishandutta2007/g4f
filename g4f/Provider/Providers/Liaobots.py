import os, uuid
from curl_cffi import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://liaobots.com'
model = ['gpt-3.5-turbo-16k', 'gpt-4-0613']
supports_stream = True
needs_auth = False
working = True

models = {'gpt-3.5-turbo-16k': {
            "id": "gpt-3.5-turbo-16k",
            "name": "GPT-3.5-16k",
            "maxLength": 48000,
            "tokenLimit": 16000
},'gpt-4-0613': {
            "id": "gpt-4-0613",
            "name": "GPT-4",
            "maxLength": 21000,
            "tokenLimit": 7000
}}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    r = requests.get("https://liaobots.lemonsoftware.eu.org/")
    try:
        authcode = r.json()['authCode']
    except:
        try:
            r = requests.get("https://liaobots.lemonsoftware.eu.org/")
            authcode = r.json()['authCode']
        except:
            authcode = 'JpuMaphc6RHUG'
    headers = {
        'authority': 'liaobots.com',
        'Pragma': 'no-cache',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Sec-Fetch-Mode': 'cors',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'content-type': 'application/json',
        'origin': 'https://liaobots.com',
        'referer': 'https://liaobots.com/zh',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
        'x-auth-code': authcode,
        'Cookie': 'gkp2=S08WPNxmmWTH61Tcajwo;cf_clearance=mFbSVO3oCzxT6s95h.9DgyqLXLbSOozEierMefagLA4-1690442944-0-250.0.0'
    }

    json_data = {
        'conversationId': str(uuid.uuid4()),
        'model': models[model],
        'messages': messages,
        'key': '',
        'prompt': "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
    }

    response = requests.post('https://liaobots.cdn.lemonsoftware.eu.org/api/chat', 
                             headers=headers,json=json_data,impersonate='safari15_5')
    yield response.text
    '''
    for token in response.iter_content(chunk_size=2046):
        yield (token.decode('utf-8'))'''

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])