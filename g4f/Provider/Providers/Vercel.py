import os
import vercel_ai
from ...typing import sha256, Dict, get_type_hints

url = 'https://sdk.vercel.ai'
supports_stream = True
needs_auth = False
working = True

models = {
'gpt-3.5-turbo':'openai:gpt-3.5-turbo', 
'gpt-3.5-turbo-16k':'openai:gpt-3.5-turbo-16k', 
'gpt-3.5-turbo-16k-0613':'openai:gpt-3.5-turbo-16k-0613',
'text-ada-001':'openai:text-ada-001', 
'text-babbage-001':'openai:text-babbage-001',
'text-curie-001':'openai:text-curie-001', 
'text-davinci-002':'openai:text-davinci-002',
'text-davinci-003':'openai:text-davinci-003',
'llama-2-7b-chat':'replicate:a16z-infra/llama7b-v2-chat',
'llama-2-13b-chat':'replicate:a16z-infra/llama13b-v2-chat',
'bloom':'huggingface:bigscience/bloom', 
'flan-t5-xxl':'huggingface:google/flan-t5-xxl', 
'gpt-neox-20b':'huggingface:EleutherAI/gpt-neox-20b', 
'oasst-sft-4-pythia-12b-epoch-3.5':'huggingface:OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5', 
'oasst-sft-1-pythia-12b':'huggingface:OpenAssistant/oasst-sft-1-pythia-12b', 
'santacoder':'huggingface:bigcode/santacoder', 
'command-light-nightly':'cohere:command-light-nightly',
'command-nightly':'cohere:command-nightly'
}
model = models.keys()

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    client = vercel_ai.Client()
    for chunk in client.chat(models[model], messages):
        yield chunk

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
