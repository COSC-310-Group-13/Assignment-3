from pickle import NONE
import pytest
from chatbot.chatbot import ChatBot as cb
import random

@pytest.fixture
def chatbot():
    chatbot = cb()
    chatbot.extractQuotes('posQuotes.txt')
    return chatbot
    
@pytest.fixture
def userHellos():
    userHellos = ['hello', "what's up", 'hey', 'hi', 'hello', 'howdy', 'sup', 'hey there']
    return userHellos

@pytest.fixture
def botHellos():
    botHellos = ['Hello', 'Good day', 'Hey!', 'Hi!', 'Nice to meet you!', 'Hello there!']
    return botHellos

@pytest.fixture
def rnd_ArrayInt():
    rndint = []
    for i in range(0,1000):
        rnd = random.uniform(0,100)
        rnd = round(rnd,5)
        rndint.append(rnd)
    
    return rndint

def test_helloMessage(chatbot, userHellos, botHellos):
    p = False  
    for i in range(0,len(userHellos)-1):
        if chatbot.helloMessage(userHellos[i]) in botHellos:
            p = True
        else:
            p = False

    assert p

def test_sortIndexList(chatbot, rnd_ArrayInt):
    sorted_rnd = chatbot.sortIndexList(rnd_ArrayInt)
    for i in range(0,len(sorted_rnd) - 2):
        if sorted_rnd[i] > sorted_rnd[i+1]:
            p = True
        else:
            P = False
    assert p

def test_botResponse(chatbot):

    dr = ["I'm sorry, I didn't quite understand what you just typed.","Sorry I'm not capable talking about that right now.",
                                  "Your choice of discussion is out of my range.", "I didn't get that could you try again?",
                                  "Unfortunealy I don't recognize what your trying to tell me."]
    if chatbot.botResponse("construction workers") in dr:
        p = False
    else:
        p = True
    assert p
