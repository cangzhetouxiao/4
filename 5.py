def test():
    message = 'Hello, welcome to my world.'
    word = 'welcome'
    if word in message:
        return message.find(word)
    else:
        return -1


print(test())
