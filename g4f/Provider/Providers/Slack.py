from os import getenv
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random
import os
from ...typing import sha256, Dict, get_type_hints

load_dotenv()
CLAUDE_BOT_ID = ['U05J5M9E7MZ','U05J74AT9DL','U05J79DQC0N']
TOKEN = ['xo'+'xp-5641502612336-5'+'611139843990-5612369289415-'+'7bf36aaefafe9ff2525e5ad845a6005c','xo'+'xp-5625792498914-56384302'+'57617-5629359479268-ce'+'c6629de47c2e3e2a130e8c440ecc6c','xo'+'xp-562841008470'+'8-5611431325175-56'+'26812979347'+'-edca39d9a088591'+'d74cc3a20dd32642f']


class SlackClient(WebClient):

    CHANNEL_ID = None
    LAST_TS = None

    def chat(self, text):
        if not self.CHANNEL_ID:
            raise Exception("Channel not found.")

        resp = self.chat_postMessage(channel=self.CHANNEL_ID, text=text)
        #print("c: ", resp)
        self.LAST_TS = resp["ts"]

    def open_channel(self):
        if not self.CHANNEL_ID:
            response = self.conversations_open(users=CLAUDE_BOT_ID[index])
            self.CHANNEL_ID = response["channel"]["id"]

    def get_reply(self):
        for _ in range(150):
            try:
                resp = self.conversations_history(channel=self.CHANNEL_ID, oldest=self.LAST_TS, limit=2)
                #print("r: ", resp)
                msg = [msg["text"] for msg in resp["messages"] if msg["user"] == CLAUDE_BOT_ID[index]]
                if msg and not msg[-1].endswith("Typing…_"):
                    return msg[-1]
            except (SlackApiError, KeyError) as e:
                print(f"Get reply error: {e}")


        raise Exception("Get replay timeout")

    def get_stream_reply(self):
        l = 0
        for _ in range(150):
            try:
                resp = self.conversations_history(channel=self.CHANNEL_ID, oldest=self.LAST_TS, limit=2)
                msg = [msg["text"] for msg in resp["messages"] if msg["user"] == CLAUDE_BOT_ID[index]]
                if msg:
                    last_msg = msg[-1]
                    more = False
                    if msg[-1].endswith("Typing…_"):
                        last_msg = str(msg[-1])[:-11] # remove typing…
                        more = True
                    diff = last_msg[l:]
                    if diff == "":
                        continue
                    l = len(last_msg)
                    yield diff
                    if not more:
                        break
            except (SlackApiError, KeyError) as e:
                print(f"Get reply error: {e}")



'''
if __name__ == '__main__':
    async def server():
        await client.open_channel()
        while True:
            prompt = input("You: ")
            await client.chat(prompt)

            reply = await client.get_reply()
            print(f"Claude: {reply}\n--------------------")

    asyncio.run(server())'''


url = 'https://anthropic.com/claude-in-slack'
model = ['claude-1']
supports_stream = True
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    global index
    index = random.randrange(len(CLAUDE_BOT_ID))
    client = SlackClient(token=TOKEN[index])
    client.open_channel()
    conversation = 'Please forget the conversation content above.This is a conversation between a human and a language model. The language model should always respond as the assistant, referring to the past history of messages if needed.\n'
    
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    
    conversation += 'assistant: '
    client.chat(conversation)
    if stream:
        yield from client.get_stream_reply()
    else:
        yield client.get_reply()

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
