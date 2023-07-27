import os
import json
import time
import subprocess
import sys
from re import findall
from curl_cffi import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://chatbot.theb.ai'
model = ['gpt-3.5-turbo']
supports_stream = True
needs_auth = False
working = True

headers = {
    'authority': 'chatbot.theb.ai',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
    'content-type': 'application/json',
    'origin': 'https://chatbot.theb.ai',
    'referer': 'https://chatbot.theb.ai/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    conversation = 'This is a conversation between a human and a language model. The language model should always respond as the assistant, referring to the past history of messages if needed.\n'
    
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    
    conversation += 'assistant: '
    json_data = {
        'prompt': conversation,
        'options': {}
    }
    response = requests.post('https://chatbot.theb.ai/api/chat-process', 
                            headers=headers, json=json_data, impersonate='chrome110')
    for chunk in response.text.splitlines():
        try:
            completion_chunk = findall(r'content":"(.*)"},"fin', chunk)[0]
            yield completion_chunk
        except:
            pass
        
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
