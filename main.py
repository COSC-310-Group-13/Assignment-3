from chatbot.chatbot import ChatBot
import sys
import PySimpleGUI as sg

# Define the window's contents
sg.theme('GreenTan')

layout = [[sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,10))],
          [sg.Text('Your Input')],
          [sg.InputText(key='i', size=(40, 2))],
          [sg.Button('SUBMIT', bind_return_key=True), sg.Button('EXIT')]]

# Create the window
window = sg.Window('Calm Bot', layout, default_element_size=(50, 3))



def __main__():
    cb = ChatBot()
    cb.extractQuotes('quotes.txt') #we establish the quotes in the object
    exitWords = ['bye', 'quit', 'exit', 'see ya', 'good bye'] #Exit the chat bot with common greetings

    while(True):    #run a loop to keep prompting the user for input
        event, values = window.read()
        print("You: "+ values['i'])
        userInput = (values['i'])
        window.FindElement('i').Update('')
        window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: "+userInput, end='')
        window['-ML1-' + sg.WRITE_ONLY_KEY].print("\n", end='')
        if event == sg.WIN_CLOSED or event == 'EXIT':
            break
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
                    break
                # Output a message to the window



    window.close()

__main__()


