import g4f

stream = True
response = g4f.ChatCompletion.create(model='dall-e', provider=g4f.Provider.Bing, messages=[
                                     {"role": "user", "content": "Hi"}], stream=stream)

if stream:
    for message in response:
        print(message)
else:
    print(response)