import requests
import os
from ...typing import sha256, Dict, get_type_hints

url = 'https://gpt4.xunika.uk/'
model = ['gpt-3.5-turbo','gpt-3.5-turbo-0301','gpt-3.5-turbo-0613','gpt-3.5-turbo-16k','gpt-3.5-turbo-16k-0613']
supports_stream = True
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer nk-wwwchatgptorguk',
        'Cookie':'FCNEC=%5B%5B%22AKsRol8oAtMdGFPKct6Xlvf9FMwt0ghzonq-NWJaGWZgyBfewG7IzKBSKZRpUeq_dOeMsER8VrYaIKOQgwwXT7zOzBtXf_OU7rD44yIjAl03Q4HRRtdsryzUPl2DuQZ8Wq6IMzD9RbCKxYuSCMqEJcDB51IiIZrqeg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; cf_clearance=Of77ONOU17lrhK7iE7EoOLEmvF0f0oansv82kv5WZ8w-1692877407-0-1-e5dbe702.bf00254.b2dab8e2-0.2.1692877407',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin':'https://gpt4.xunika.uk',
        'Referer':'https://gpt4.xunika.uk/'
    }
    data = {
        'model': model,
        'temperature': kwargs.get("temperature", 0.7),
        'presence_penalty': kwargs.get('presence_penalty', 0),
        'top_p':1,
        'frequency_penalty': 0,
        'messages': messages,
    }
    response = requests.post('https://gpt4.xunika.uk/api/openai/v1/chat/completions',
                             json=data, headers=headers,stream=True)
    
    yield response.json()['choices'][0]['message']['content']

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])