import requests
import time
from translate import Translator
import os
from ...typing import sha256, Dict, get_type_hints

url = 'https://editor.fusionbrain.ai/'
model = ['kandinsky']
supports_stream = True
needs_auth = False
working = True

HEADERS = {
    "accept-language": "en-US,en;q=0.9",
    "referrer": "https://editor.fusionbrain.ai/",
    "origin": "https://editor.fusionbrain.ai",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    q = messages[-1]['content']
    qt = Translator(from_lang ='autodetect',to_lang="en").translate(q)
    if qt == 'PLEASE SELECT TWO DISTINCT LANGUAGES':
        qt=q
    boundary = '----WebKitFormBoundaryAvV9KCrOGx8dToxn'
    data_list = [
    f'--{boundary}\r\n',
    'Content-Disposition: form-data; name="params"; filename="blob"\r\n',
    'Content-Type: application/json\r\n',
    '\r\n',
    '{"type":"GENERATE","style":"DEFAULT","width":1024,"height":1024,"generateParams":{"query":"'+qt+'"}}\r\n', 
    f'--{boundary}--'
    ]
    data = ''.join(data_list)
    HEADERS['Content-Type']= f'multipart/form-data; boundary={boundary}'
    r = requests.post("https://api.fusionbrain.ai/web/api/v1/text2image/run?model_id=1",headers=HEADERS, data=data)
    try:
        id = r.json()['uuid']
    except:
        yield 'Image generation error. This may be because your image is illegal or our service has malfunctioned.'
        return
    r = requests.get("https://api.fusionbrain.ai/web/api/v1/text2image/status/"+id,headers=HEADERS)
    img = r.json()['images']
    t = 0
    while img == None and t<30 :
        time.sleep(0.5)
        t += 0.5
        r = requests.get("https://api.fusionbrain.ai/web/api/v1/text2image/status/"+id,headers=HEADERS)
        img = r.json()['images']
    if not img:
        yield 'Image generation error. This is because our service has malfunctioned.'
        return
    yield '![](data:image/png;base64,'+img[0]+')'


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])