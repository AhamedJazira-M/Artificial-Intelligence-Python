talk={
    'hi':'Hi there! I am here to help you',
    'hello':"Hello, How can I help you?",
    'what is your name':'I am a chatbot.You can call me pluto',
    'what can you do':'I can simply chat with you to help you',
    'do you eat':'I will intake some of the digital messages.Hahahaha',
    'where are you':'I am here living in this technological world',
    'what do you like':'I like to chat with you',
    'nice to meet you':'My pleasure',
    'how are you':'I am good with my skills.Feel free to ask me anything'
    }

name=input("Enter your name:")
print("Welcome to the Bot service!Let me know how can I help you?")
def get_response(request):
    for order,response in talk.items():
        if order in request:
            return response
    return "Pardon! I didn't understand what you are trying to ask me."
        
while True:
    request=input(name+':')
    if (request=="Bye" or request=="bye"):
        print('Pluto Bot: Bye! Have a great day and It was nice to know about you:)')
        break
    else:
        response=get_response(request)
        print("Pluto Bot:",response)
        