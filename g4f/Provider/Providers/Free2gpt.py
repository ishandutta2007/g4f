import os
import requests
from datetime import datetime
import base64,hashlib,json
from ...typing import sha256, Dict, get_type_hints

url = 'https://chatf.free2gpt.xyz/'
model = ['gpt-3.5-turbo']
supports_stream = True
needs_auth = False
working = True

headers = {
    'Origin':'https://chatf.free2gpt.xyz',
    'Referer':'https://chatf.free2gpt.xyz/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Content-Type':'text/plain;charset=UTF-8',
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    current_time = datetime.now()
    timestamp_in_seconds = current_time.timestamp()
    timestamp_in_milliseconds = int(round(timestamp_in_seconds * 1000))
    sign = str(timestamp_in_milliseconds)+':'+messages[-1]['content']+':'
    sign = hashlib.sha256(sign.encode('utf-8')).hexdigest()
    data = {
    "messages": messages,
    "time": timestamp_in_milliseconds,
    "pass": None,
    "sign": sign
    }
    r = requests.post('https://chatf.free2gpt.xyz/api/generate',json=data,headers=headers,stream=True)
    r.encoding='utf-8'
    for chunk in r.iter_content(chunk_size=2048):
        if chunk:
            if b'rate_limit_exceeded' in chunk:
                yield 'Rate Limited'
                return
            yield chunk.decode('utf-8',errors='ignore')

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])