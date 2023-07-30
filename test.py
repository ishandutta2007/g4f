import g4f

stream = True
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=g4f.Provider.Theb, messages=[
                                     {"role": "user", "content": "Hi"}], stream=stream)

if stream:
    for message in response:
        print(message,end="")
else:
    print(response)