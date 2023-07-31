import g4f

stream = True
response = g4f.ChatCompletion.create(model='llama-2-7b-chat', provider=g4f.Provider.PerplexityAI, messages=[
                                     {"role": "user", "content": "Hi"}], stream=stream)

if stream:
    for message in response:
        print(message,end="")
else:
    print(response)