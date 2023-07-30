import sys
import json
import re
from curl_cffi import requests

config = json.loads(sys.argv[1])
model = config['model']
prompt = config['messages'][-1]['content']
if model == 'gpt-4-0613':
    json_data = json.dumps({
  "userInput": "Hi",
  "messages": [],
  "anonUserID": ""
}, separators=(',', ':'))
    headers = {
    "accept": "*/*",
    "baggage": "sentry-environment=vercel-production,sentry-release=17ac4575f09a70b6d11b370305c5c232ccc740ff,sentry-transaction=%2Fagent,sentry-public_key=ea29c13458134fd3bc88a8bb4ba668cb,sentry-trace_id=cae48a5201194de9897c90a959cb41fd,sentry-sample_rate=0.002,sentry-replay_id=c622e21e115345c69aaa723c253ae4c3",
    "content-type": "application/json",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "cae48a5201194de9897c90a959cb41fd-89e44f68ac2353d8-0",
    'Content-Type': 'application/json',
    'Pragma': 'no-cache',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.phind.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Referer': 'https://www.phind.com/agent',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Cookie':'__cf_bm=_IRj.8NM5j8u7IXNCeQeYQO6pKEA6fH8zr8glrr_9wo-1690733956-0-AXDTsLVChYgL7QF/88zm0HjZdKYsp23RwRpWG4JsfBWooKmNZQ8jWjLaYQYY/ihIoJxwj8pS677lOaCP/x5WRps=; __Host-next-auth.csrf-token=56f1687f951dd514127f7f09835943ac71b43b7c8df5c07fe9f83e8ab2b1a953%7Cb68332e0f2950cf104ccebfa4cc7e8590e6e5b0e8f388d0ac4cb42f8094eb5bd; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.phind.com%2F; cf_clearance=PeV3_ME4QtJyFf35LHuSRnL.ckXbTfQndUSQgTMXJGw-1690733963-0-1-9895f01e.b9c64471.cf94affe-0.2.1690733963; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..eqiHzSErquEy5J8x.YoB-z5B1HDdJoO3zWROuTWHJM6WHHJFht6GEZQonrT0jNBBc4Jn-2Pp9Y39MkbZ8bW0NqoVDShkDtWrvxBjdzrGQYoFB6VX6akuN1gG2aqY1Jol6kuBWnLS3jp8felzIsy77hJB2INB67H269eQdLj14LUZ82fJVe6na7v_tUpqbmja5Imqs2DRU1xbwGzxYywJAWMAFE1WtoOuWk1hj0RSTw9u9zGPO8EU.pwDJCOV1_WEPxZPaO1tD3A; mp_6d31cd4238973a84421371ef3929c915_mixpanel=%7B%22distinct_id%22%3A%20%22189a798d5dd21-0ab4e9da64dd5d-26031c51-144000-189a798d5deeb4%22%2C%22%24device_id%22%3A%20%22189a798d5dd21-0ab4e9da64dd5d-26031c51-144000-189a798d5deeb4%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22clkpndx060021mq08b65lvanf%22%7D'
  }
else:
    json_data = json.dumps({
            "userInput": prompt,
            "messages": config['messages'],
            "shouldRunGPT4": False
        }, separators=(',', ':'))

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

def output(chunk):
    try:
        if b'PHIND_METADATA' in chunk:
            return
        
        if chunk == b'data:  \r\ndata: \r\ndata: \r\n\r\n':
            chunk = b'data:  \n\r\n\r\n'

        chunk = chunk.decode().strip()
        chunk = chunk.replace('data: \r\n\r\ndata: ', 'data: \n')
        chunk = chunk.replace('\r\ndata: \r\ndata: \r\n\r\n', '\n\r\n\r\n')
        chunk = chunk.replace('data: ', '').replace('\r\n\r\n', '')
        if chunk.count('[{"index": 0, "delta": {"content":')>0:
            for completion_chunk in re.findall(r'"model": "'+model+'", "choices": \[{"index": 0, "delta": {"content": "(.*?)"}, "fin', chunk):
                print(completion_chunk.replace('\\n','\n'),flush=True,end="")

    except Exception as e:
        pass


try:
    response = requests.post('https://www.phind.com/api/agent',
                        headers=headers, data=json_data, content_callback=output, timeout=999999, impersonate='safari15_5')
    
    exit(0)

except Exception as e:
    print('Error')