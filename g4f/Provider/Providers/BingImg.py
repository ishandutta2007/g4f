import requests
import time
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import os
from ...typing import sha256, Dict, get_type_hints

url = 'https://bing.lemonsoftware.eu.org/images/create?FORM=GDPGLP'
model = ['dall-e']
supports_stream = True
needs_auth = False
working = True

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "referrer": "https://www.bing.com/images/create/",
    "origin": "https://www.bing.com",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edge/110.0.1587.63",
}

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    q = messages[-1]['content']
    params = {
        't':int(round(time.time() * 1000)),
        're': 1,
        'showselective': 1,
        'sude': 1,
        'kseed': 7500,
        'SFX': 2,
        'q': q
    }
    
    r = requests.get("https://bing.lemonsoftware.eu.org/images/create",params=params,headers=HEADERS)
    try:
        id = urlparse.parse_qs(urlparse.urlparse(r.url).query)['id'][0]
    except:
        yield 'Image generation error. This may be because your image is illegal or our service has malfunctioned.'
        return
    image_urls = set()
    t = 0
    while len(image_urls)<4 and t<40:
        time.sleep(0.5)
        t += 0.5
        r = requests.get("https://bing.lem0n.eu.org/images/create/async/results/"+id+"?q="+params['q'],headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            src = img_tag.get('src')
            if src:
                image_urls.add(src)
    if not image_urls:
        yield 'Image generation error. This is because our service has malfunctioned.'
        return
    for img in image_urls:
        yield '![]('+img+')'


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])