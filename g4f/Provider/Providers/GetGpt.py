import os
import json
import uuid
import requests
from Crypto.Cipher import AES
from ...typing import sha256, Dict, get_type_hints

url = 'https://chat.getgpt.world/'
model = ['gpt-3.5-turbo']
supports_stream = True
needs_auth = False
working = False


def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    def encrypt(e):
        t = os.urandom(8).hex().encode('utf-8')
        n = os.urandom(8).hex().encode('utf-8')
        r = e.encode('utf-8')
        cipher = AES.new(t, AES.MODE_CBC, n)
        ciphertext = cipher.encrypt(pad_data(r))
        return ciphertext.hex() + t.decode('utf-8') + n.decode('utf-8')

    def pad_data(data: bytes) -> bytes:
        block_size = AES.block_size
        padding_size = block_size - len(data) % block_size
        padding = bytes([padding_size] * padding_size)
        return data + padding

    headers = {
        'Content-Type': 'application/json',
        'Referer': 'https://chat.getgpt.world/',
        'Token': '03AAYGu2S1OBCUWWUUkfc9zdmWxZbBcCPVx6Bja6hVz83xdg5fgmo5azbPnZS8h2qkds4zpYNINwh6dK0zYmu4BZ1_t42r8E3hT73am5Fut1WckoyOBMeha25lDiuGbeDonjHgCdn9ve8zaS-H-892jt5CmUv3ny4M13g5xrPrT0PlyzK5wMP8Lbn94qZwiaF7ys5LKehXNhyAx7OgHSzcC9GGMAbQPekulvdFRzUNDx9zwiHMnOqzRydCWvm3VmEcMYUT6C9wK7_uCApvpkZ6l5fEmLjJL4Im5h9nLnGCuJma8nlLMBdGCVFtF_Jt0NPwS0QwpfksQIkOrN44JxUj8vezzmlhqMgR3NTipTUyqb7ZjfuE2vdzlEaMAMosnMi4BX6eruw5yDrF2l3mVmZk4C-tlljMBm5MCoskh72_9ou4A3tWpxKbslNb_pse5ECTWe13lAoQU-ZoexAqovI7fXUhd4EeJSdU42UWetZHpOEXCsy-hCFQ0TwDemNnT_7ACPDcbJqkqY1NkBjjOHNLfa0ZDMT7kLkofHiu2lxm9DXA-t79AzmNF56hHupYPSYg14QwIiStTRiMVwpl79tzIysNGF5iKDnRIiX76HvylAhNtuarfZZsspKTWVtsM7pbl7KlZsc4GfEuehUvgGel2M1aBZOjbZrYWBQn5C7bYhM7LOjVttryQpffIP-E2juuogR6EM6V0IkdgvlL0nuvShxIkYsHPvTEOcaGoXRYgEsiHH4hsjbMJqBgKr8bFeGHOHCRAf-2klfrMVWmK9ZzL5r3D6l0bNAXPZ45d33VbU9LXo543lAXxSCaND12Il1Y_IM4Dl59shWd8NZeUVkYISJY69r1bTm7HmzTyhnG-PN3j9AiT7TdzKf40XhsBNw6gsBpmkPdxD3H9RcvyfzzWBYojuB1X43ZZs2AMitmho0bzC7XyDq1YFVoRHVclwzpEY4Vx--reBiCp1TYSe19qRXmHecRLWYuw37f5VLJH_YB2LFcxdu0CeSgXc1IEzIdJq6W5YzQlugQ6yhusOPO8JUeXEv24dwd5DHRAf7XVC2OVKU9FORBHQtmO5BbERQQHXmk1_NDCkgAGO_yMAIWQ8k1jKTCiu59oSHqZ0KTJSGtGAdiN95J_lpT0rswAITR7Nou0m4zw-M9WFrhdrlYFeIMA4dQmxdnk81Nzlzp5j_KbQ5pJWVfex9gU-uGTFCYj8uA_DhUGbW3SZYZ_Fvze03ZrqeGC05Qcc8xn_pmQpANsrIKPunO9CPspk9jQ5dw2urfsbQtyC_y0gtYzMRMKGhI1kMPTL2yu2wdLvAdELE75mCvcnQiT3hfgLCXIOqFwDPnQc7aU1CF3RFC9SB41KvPzNO7j2ZitUnqpElZZeTl-d-hH0dCxvftmuQyy73pFs8qeShZm0FNmOUn_G2006-1maxd1KfwFbD4EMYESo9Jcf1gVlbNPfiPrnackFCiDDOSYNfnyxoOmni-D-Dz_DU98FOmWrXYbbuvSMi92RGjcYgrKezSgEue-vZUI0-WRjM9XIvHS3hUCrrhTFXVik9Fg5HM-etgllzB1ox6Au_bHyqWV3SuUYO5e6iBXKSnYaaRmHXwUy1KrRhjvSyuXK9Os-9QAmNp1c3B7sVmjIpC-99sNfekzfMKms3e9BYxOLaMYNvKtUhYd1nCKo1mwq_ldht3pkyr909Nk_vO6rN78EJMyTNBiCAqDcFUgXozSaJfGZteLPc_AGoY8fBMOucnHs6kCjm_Bmf7NPdDakYmkXba_9AuJ7ysTWw691wCV4bGV-hMfY3v',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    data = json.dumps({
        'messages': messages,
        'frequency_penalty': kwargs.get('frequency_penalty', 0),
        'max_tokens': kwargs.get('max_tokens', 4000),
        'model': 'gpt-3.5-turbo',
        'presence_penalty': kwargs.get('presence_penalty', 0),
        'temperature': kwargs.get('temperature', 1),
        'top_p': kwargs.get('top_p', 1),
        'stream': True,
        'uuid': str(uuid.uuid4())
    })

    res = requests.post('https://chat.getgpt.world/api/chat/stream', 
                        headers=headers, json={'signature': encrypt(data)}, stream=True)

    for line in res.iter_lines():
        if b'content' in line:
            line_json = json.loads(line.decode('utf-8').split('data: ')[1])
            yield (line_json['choices'][0]['delta']['content'])


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f'{name}: {get_type_hints(_create_completion)[name].__name__}' for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
