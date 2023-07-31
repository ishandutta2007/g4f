import subprocess
import json
import os
from ...typing import sha256, Dict, get_type_hints

url = 'https://labs.perplexity.ai/'
model = ['llama-2-7b-chat','llama-2-13b-chat','llama-2-70b-chat']
supports_stream = True
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    path = os.path.dirname(os.path.realpath(__file__))
    config = json.dumps({
        'model': model,
        'messages': messages}, separators=(',', ':'))
    cmd = ['python3', f'{path}/helpers/perplexityai.py', config]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        if b'<title>Just a moment...</title>' in line:
            os.system('clear' if os.name == 'posix' else 'cls')
            yield 'Error'
            os._exit(0)
        else:
            yield line.decode('unicode_escape',errors='ignore') #[:-1]
            
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])