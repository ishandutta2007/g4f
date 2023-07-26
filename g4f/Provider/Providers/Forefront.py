import os
import json
import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://chat.forefront.ai/'
model = ['gpt-3.5-turbo','claude-instant']
supports_stream = True
needs_auth = False
working = True


def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    conversation = 'This is a conversation between a human and a language model. The language model should always respond as the assistant, referring to the past history of messages if needed.\n'
    
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    
    conversation += 'assistant: '

    json_data = {
        'text': conversation,
        'hidden': True,
        'action': 'new',
        'id': '379e1b22-18da-b4b9-00da-830cdc2a9210',
        'parentId': '79dcec9e-3b7b-4c39-b967-00285b1cd22b',
        'workspaceId': '79dcec9e-3b7b-4c39-b967-00285b1cd22b',
        'messagePersona': 'default',
        'model': model,
        'messages': messages[:-1] if len(messages) > 1 else [],
        'internetMode': 'never'
    }

    headers = {'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Imluc18yTzZ3UTFYd3dxVFdXUWUyQ1VYZHZ2bnNaY2UiLCJ0eXAiOiJKV1QifQ.eyJhenAiOiJodHRwczovL2NoYXQuZm9yZWZyb250LmFpIiwiZXhwIjoxNjkwMzU0ODYyLCJpYXQiOjE2OTAzNTQ4MDIsImlzcyI6Imh0dHBzOi8vY2xlcmsuZm9yZWZyb250LmFpIiwibmJmIjoxNjkwMzU0NzkyLCJzaWQiOiJzZXNzXzJUNjlQWFo4VEpyb2lmMldmMHlpeU1TOXlPdiIsInN1YiI6InVzZXJfMlQ2OVBZdGNYeXBBa0Q3UDl1a1ZQTkdGWDRGIn0.bxp-NUcGfGvKHqTl6FYCVUrPVtLTSNfwAKCDVEesp2by2y2UFhTX7iDwbkNh4OzJtJglsdIo2sKvyiuBCoVDGHmPKSjD3D62FXC7xEaXaJ6EQuhgDgpMin4qlAoCUvYWSy9KQRW0YCcIqhJ65-u3XvKT610G2RSt70vf4Bwhu9q-LRdd4YEIXvtBd2BIQOm9daLG1w5qTb0xwegDJaWp4rocf5ey64XvxJVoXEMgIgOW6LxfMl9n6hUe7artfkVNiEFnNWp9lc-zW-h8uSk9u6DTCQuOJEURnRcrV55PJJXLa7lxgt70bNsABCt60ewo8JLjL9iDdK3kGgtvFaj3eQ'}
    response = requests.post('https://streaming-worker.forefront.workers.dev/chat',
        json=json_data, stream=True,headers=headers)
    print(response.text)
    for token in response.iter_lines(): 
        if b'delta' in token:
            token = json.loads(token.decode().split('data: ')[1])['delta']
            yield (token)
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])