import os
import json
import time
from curl_cffi import requests
#import subprocess

from ...typing import sha256, Dict, get_type_hints

url = 'https://phind.com'
model = ['gpt-3.5-turbo-0613']
needs_auth = False
supports_stream = True
working = True

headers = {
    'Content-Type': 'application/json',
    'Pragma': 'no-cache',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.phind.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Referer': 'https://www.phind.com/agent',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Cookie': '__Host-next-auth.csrf-token=b254c36d29862b95381910bd789b890dc081c9745fbe8b397487b55ded503d50%7C5e97dfca46c3a263e180c6dffa4c315464b232d1e4dbd81340c66d98eb4c6241; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.phind.com; mp_6d31cd4238973a84421371ef3929c915_mixpanel=%7B%22distinct_id%22%3A%20%22188c4960b0afd1-04505a4573c948-26031d51-144000-188c4960b0b916%22%2C%22%24device_id%22%3A%20%22188c4960b0afd1-04505a4573c948-26031d51-144000-188c4960b0b916%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fgithub.com%2Fxiangsx%2Fgpt4free-ts%2Fblob%2Fmaster%2FREADME_zh.md%22%2C%22%24initial_referring_domain%22%3A%20%22github.com%22%7D; cf_clearance=8LxWcAZIbce1P814klBXEYGb7_0EJ0rzcMcskzm1eJ4-1690435153-0-1-efb0c65b.1c588b13.b8b199bb-0.2.1690435153; __cf_bm=oBEN3D2yv7CYMOZwb0bE7tM.qQpb92OWckfYZfxRk3g-1690435155-0-ATa9DlpuUspsHjm1DPWKiOK6yNeTddtyhtmVwb/VCrXi4EBkansL9lGaC2+ZklFzPZnivkdQZ+mZJADHJFqXl3g='
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    data = json.dumps({
        "userInput": messages[-1]['content'],
        "messages": messages,
        "shouldRunGPT4": False
    })
    r = requests.post('https://www.phind.com/api/agent',headers=headers,data=data,impersonate='safari15_5')
    for chunk in r.text.splitlines():
        if chunk:
            data = json.loads(chunk.split('data: ')[1])
            if 'user.message' not in data['id']:
                try:
                    if data['choices'][0]['delta']['content'] and data['choices'][0]['delta']['content'] != 'Using other Agent.':
                        yield data['choices'][0]['delta']['content']
                except:
                    pass
    '''
    path = os.path.dirname(os.path.realpath(__file__))
    config = json.dumps({
        'model': model,
        'messages': messages}, separators=(',', ':'))

    cmd = ['python3', f'{path}/helpers/phind.py', config]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in iter(p.stdout.readline, b''):
        if b'<title>Just a moment...</title>' in line:
            os.system('clear' if os.name == 'posix' else 'cls')
            yield 'Clouflare error, please try again...'
            os._exit(0)
        
        else:
            if b'ping - 2023-' in line:
                continue
            
            yield line.decode('cp1251') #[:-1]
         '''   
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
