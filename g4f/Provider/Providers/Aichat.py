import os
from curl_cffi import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://chat-gpt.org/chat'
model = ['gpt-3.5-turbo']
supports_stream = False
needs_auth = False
working =  True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    base = ''
    for message in messages:
        base += '%s: %s\n' % (message['role'], message['content'])
    base += 'assistant:'
    
    
    headers = {
        'authority': 'chat-gpt.org',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://chat-gpt.org',
        'pragma': 'no-cache',
        'referer': 'https://chat-gpt.org/chat',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Cookie':'XSRF-TOKEN=eyJpdiI6InJqNG4xZ05mMW9nRVNvL1p4Nkt3S3c9PSIsInZhbHVlIjoiUVVUS0h0YjlsS2l4Vzg0K3FVcEdpMkRIOWRmOVRnZjF0UHpXZVVNcGR3cVFDK0lJRjVEVHBPZmhRSVZXL1d6SGgwVTFva2gwaHlFaVVTdnNuNElJQ0FzNjB5eHZ0N3NWOUQyenBaMUJ0c1RmY3pKUGxLaHlIbitNR21JMHZ4ZnciLCJtYWMiOiIxZDhkNWIyZmZiODc0MTEzOTdmZjg1OTNjZDMxNzBhNTVlYjc3NzVhMjY4NWUxNGRlMjJlOGYxZjNiMDg2YjkxIn0%3D; chatgptchatorg_session=eyJpdiI6IlpmaUV4dVVZZm9GTHFtNmFEaTlvT1E9PSIsInZhbHVlIjoiZ28wcUpEYXRyNC94VjYwc1BwVnBXNElxMkphajRMRTFlMW43N3dWZ2JMdFhNTEh5YmJFT1AzRTNRbUQxVVo3SnBiN3c5V1N1ZnMrcGtVcGRQT1Jtekd3TWF3NHZDMnMweVlVMDU0SFBJLzFaMTgwSTBiWVA5eWJBTXJ5TXBBRW8iLCJtYWMiOiI2MmMwZTcwZWUzYjk1Yjk2NmNlZWFiYzQ2NzNiYjE4NzQ2YWQ1ZDVjMTljMjIyNzI2ZWM3ZTUxZmYxMzY2NDU5In0%3D; cf_clearance=IERj8_nuFs9IYmUaK39KxwUnoFc9.bFDZ96KbWODjoc-1690707463-0-0.2.1690707463'
    }

    json_data = {
        'message':base,
        'temperature': 1,
        'presence_penalty': 0,
        'top_p': 1,
        'frequency_penalty': 0
    }
    
    response = requests.post('https://chat-gpt.org/api/text', headers=headers,impersonate='chrome110',json=json_data)
    yield response.json()['message']

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])