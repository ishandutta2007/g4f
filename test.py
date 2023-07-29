import g4f

stream = False
response = g4f.ChatCompletion.create(model='gpt-4', provider=g4f.Provider.Bing, messages=[
                                     {"role": "user", "content": "Hi"}], stream=stream)

if stream:
    for message in response:
        print(message)
else:
    print(response)