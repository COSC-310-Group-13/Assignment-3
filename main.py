
import PySimpleGUI as sg

# Define the window's contents
sg.theme('GreenTan')

layout = [[sg.Text('Your Input')],
          [sg.InputText(key='i', size=(40, 2))],
          [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,10))],
          [sg.Button('SEND'), sg.Button('EXIT')]]

# Create the window
window = sg.Window('Very Complex GUI', layout, default_element_size=(50, 3))

# Display and interact with the Window using an Event Loop


# Finish up by removing from the screen
from chatbot.chatbot import ChatBot
from chatbot.spellcheck import SpellCheck
import sys
import PySimpleGUI as sg
import subprocess
# Define the window's contents
sg.theme('Dark2')

layout = [[sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,10))],
          [sg.Text('Your Input')],
          [sg.InputText(key='i', size=(40, 2))],
          [sg.Button('SUBMIT', bind_return_key=True), sg.Button('EXIT')]]

# Create the window
window = sg.Window('Calm Bot', layout, default_element_size=(50, 3),finalize=True)

def __main__():
    sc = SpellCheck()
    cb = ChatBot()
    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")
    cb.extractQuotes('quotes.txt') #we establish the quotes in the object
    exitWords = ['bye', 'quit', 'exit', 'see ya', 'good bye'] #Exit the chat bot with common greetings

    exitError = sp.errorHandlingArray(exitWords) # correcting for errors

    while(True):    #run a loop to keep prompting the user for input
        event, values = window.read()
        print("You: "+ values['i'])
        userInput = (values['i'])
        window.FindElement('i').Update('')
        window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: "+userInput, end='')
        window['-ML1-' + sg.WRITE_ONLY_KEY].print("\n", end='')
        if event == sg.WIN_CLOSED or event == 'EXIT':
            sys.exit()
        if userInput.lower() in exitWords:
            window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: It was really nice talking to you!", end='')
            window['-ML1-' + sg.WRITE_ONLY_KEY].print("\n", end='')
            print("Calm Bot: It was really nice talking to you!")
            sys.exit()
        else:
            if cb.helloMessage(userInput) != None:  #if hello returns nothing, output a quote
                out=("Calm Bot: " + cb.helloMessage(userInput))
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='')
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("\n", end='')
            else:
                out = ("Calm Bot: " + cb.botResponse(userInput))
                print(out)
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='')
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("\n", end='')
                event, values = window.read()
                # See if user wants to quit or window was closed
                if event == sg.WINDOW_CLOSED or event == 'Quit':
                    sys.exit()

__main__()


