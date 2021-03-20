from chatbot.chatbot import ChatBot
import sys

#Main class where the bot will be run from.


def __main__():
    cb = ChatBot()
    cb.extractQuotes('quotes.txt') #we establish the quotes in the object

    exitWords = ['bye', 'quit', 'exit', 'see ya', 'good bye'] #Exit the chat bot with common greetings

    while(True):    #run a loop to keep prompting the user for input
        print("You: ", end ='')     
        userInput = input()     #Ask user for input
        if userInput.lower() in exitWords:
            print("Calm Bot: It was really nice talking to you!")
            sys.exit()
        else:
            if cb.helloMessage(userInput) != None:  #if hello returns nothing, output a quote
                print("Calm Bot: " + cb.helloMessage(userInput))
            else:
                print("Calm Bot: " + cb.botResponse(userInput))


__main__()
