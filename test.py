import g4f

stream = True
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo-0613', provider=g4f.Provider.Phind, messages=[
                                     {"role": "user", "content": "Hi"}], stream=stream)

if stream:
    for message in response:
        print(message)
else:
    print(response)