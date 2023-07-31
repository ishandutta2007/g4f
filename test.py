import g4f

stream = True
response = g4f.ChatCompletion.create(model='claude-instant-100k', provider=g4f.Provider.B88, messages=[
                                     {"role": "user", "content": "write a poem in english about apples"}], stream=stream)

if stream:
    for message in response:
        print(message,end="")
else:
    print(response)