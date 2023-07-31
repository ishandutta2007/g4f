import base64
import os
import json
import sys
import socketio
config = json.loads(sys.argv[1])
model = config['model']
messages = config['messages']
def generate_sec_websocket_key():
    random_bytes = os.urandom(16)
    sec_websocket_key = base64.b64encode(random_bytes).decode('utf-8')
    return sec_websocket_key
output = ''

key = generate_sec_websocket_key()
sio = socketio.Client()
@sio.on(model+'_query_progress')
def chat(data):
    global output
    if data['final']:
        sio.disconnect()
    print(data['output'][len(output):],flush=True,end='')
    output = data['output']
sio.connect("https://labs-api.perplexity.ai",headers={"Accept-Language": "q=0.9,en-US;q=0.8,en;q=0.7","Cache-Control": "no-cache","Pragma": "no-cache","Sec-WebSocket-Extensions": "client_max_window_bits","Sec-WebSocket-Key": key,"Sec-WebSocket-Version": "13","Upgrade":"websocket","Connection":"Upgrade","Origin":"https://labs.perplexity.ai","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})
sio.emit('perplexity_playground', {'model': model, 'messages': messages})