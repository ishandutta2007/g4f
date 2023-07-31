import os
import requests
from datetime import datetime
import base64,hashlib,json
from ...typing import sha256, Dict, get_type_hints

url = 'https://powerchat.top/'
model = ['gpt-3.5-turbo']
supports_stream = True
needs_auth = False
working = True

headers = {
    'Origin':'https://powerchat.top',
    'Referer':'https://powerchat.top/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Content-Type':'text/plain;charset=UTF-8',
    'Version':'1.0'
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    current_time = datetime.now()
    timestamp_in_seconds = current_time.timestamp()
    timestamp_in_milliseconds = int(round(timestamp_in_seconds * 1000))
    sign = str(timestamp_in_milliseconds)+':question:contact_me_to_work_together_hello@promptboom.com'
    sign = hashlib.sha256(sign.encode('utf-8')).hexdigest()
    data = '{"did":"060ca8eaa0625da25d61ae94d4a2cf99","chatList":'+json.dumps(messages)+',"special":{"time":'+str(timestamp_in_milliseconds)+',"sign":"'+sign+'","referer":"https://github.com/","path":"https://powerchat.top/"}}'
    data = base64.b64encode(data.encode('utf-8')).decode()
    r = requests.post('https://api.powerchat.top/requestPowerChat',json={'data':data},headers=headers,stream=True)
    for chunk in r.iter_content(chunk_size=2048):
        if chunk:
            yield chunk.decode(errors='ignore')

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])