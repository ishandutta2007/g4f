import os, requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://ora.ai'
model = ['gpt-3.5-turbo']
supports_stream = False
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    conversation = 'This is a conversation between a human and a language model. The language model should always respond as the assistant, referring to the past history of messages if needed.\n'
    
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    
    conversation += 'assistant: '
    headers = {
        'authority': 'ora.ai',
        'accept': '*/*',
        'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://ora.ai',
        'pragma': 'no-cache',
        'referer': 'https://ora.ai/chat/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Cookie': '__stripe_mid=a56e924b-2fc8-4a5a-bd45-2a9b2f90c821ae1cc2; __Host-next-auth.csrf-token=5cfe1760706ca06210042149383b3ef22aaa5846762b44db421e8d38c4423966%7C4598f1661f9b11c1a8c90f76f3491815313d4be68c848eaffbf6fed7f2277448; cf_clearance=9Z1Wsk0X0173vYlaeQl.q1cDTuFKT.YFdwLG6W0_b2o-1690368510-0-0.2.1690368510; __Secure-next-auth.callback-url=https%3A%2F%2Fora.ai%2F; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..zIWD47JAHuA3EFF-.3PpRlDf0SABTw2Lf98fwwptXhBcN-O0hGk3H_Qugk3miLcGWIUoFWOVbByITZl5xBfZH1uoG4Tbvc_U7v5BPRBDMmty9a9slhSors6aPnrw69HH2piUSD_UVMK-L_jTMGQX-aw8OzF7yUM9e6Sy3fKt86nW7NcFsdky9ujfPMWZSwYR4J4FA0ErOGX25ofxsUyrVqeDRTngZzmT9pV_ndY7EVJWXFyBsszDzHOPTGbjU4zIQVxmgeMuGGnYlBMs0KSnBB8zrt811_-_vFakhStTYTpwO5L1u4zPolyfqNWowCfmQzDhlKnIFUb3NFG_R0dAapcBvsb8CoZ2Bo-miMAJTaKOT2oyEGek-XjWATbH8V-88LHI8O1qIQXWw25TgxuCiPnsuye8EpMPSJ4HDNOjgO6QyosUkH5nT9ucwrPh_9BgUdrPrAhcARE1YJSVv7v1tB28kz9p8u0w7nvuVAcUxJQXRtZWDxSigCc-NpQbDow0IsB2TvKKv-OOXKU30XrB1ituHLrtPqcytyGrJgaXVJhVgGUF-74pd6ccZ0TYS3piKTNkwTEfLywAs2ASjfxQiwwvDtDxGvuU5IBD1av8JHCJ0st6p_6NTPxXVBsyuE4KLNzz2T9e7NHThyZfzlqnlmIgP-HbHu5AtWaRXkqmevyM.6XqeOjjFbNjGyNTAQN5G_Q; __stripe_sid=edfafaaf-0868-41bb-a45c-5f425d33ab6b0e0a23'
    }

    json_data = {
        'chatbotId': 'c38a3119-3ee3-474b-b3a6-9f811e291325',
        'input': conversation,
        'userId': 'c26561a7-7755-485a-8ad3-38071f0d42f0',
        'provider': 'OPEN_AI',
        'config': False,
        'includeHistory': False
    }

    response = requests.post('https://ora.ai/api/conversation', 
                            headers=headers, json=json_data)
    
    yield response.json()['response']

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])