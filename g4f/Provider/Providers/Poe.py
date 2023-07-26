import os
import random
import poe
from ...typing import sha256, Dict, get_type_hints

url = 'https://poe.com/'
models = {'gpt-3.5-turbo':'capybara','claude-instant':'a2','palm':'acouchy','palm2':'acouchy','bard':'acouchy','google-bard':'acouchy','google-palm':'acouchy'}
model = ['gpt-3.5-turbo','claude-instant','palm2']
supports_stream = True
needs_auth = False
working = True
token = ['H959lSH8kjQ-b4K8FCrDPg%3D%3D','ACHY1MG7xz1yE0P6EByF5g%3D%3D','a4DoOVnIl3FievhYiQYOJw%3D%3D']
formkey = ['a40f267a9751c48d34c9f12f56c5c6f8','b65db0a463062fcabe43aa6c6978c344','413b8fa39bfb54f99cb9a4f18d18aab1']
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    path = os.path.dirname(os.path.realpath(__file__))
    conversation = '这是一个人和一个语言模型之间的对话。语言模型应该始终作为助理进行响应，如果需要，可以参考过去的消息历史。\n'
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    conversation += '助理: '
    index = random.randrange(len(token))
    client = poe.Client(token[index],formkey=formkey[index])
    for chunk in client.send_message(models[model], conversation, with_chat_break=True):
        yield chunk["text_new"]
    client.purge_conversation(models[model], count=3)

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])