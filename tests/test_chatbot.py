from pickle import NONE
import pytest
from chatbot.chatbot import ChatBot as cb
import random

#Load in reused classes and variables
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

#Tests the helloMessage method by making sure the bot regocnizes all predetermined user greetings
def test_helloMessage(chatbot, userHellos, botHellos):
    p = False  
    for i in range(0,len(userHellos)-1):
        if chatbot.helloMessage(userHellos[i]) in botHellos:
            p = True
        else:
            p = False

    assert p

#tests this function by giving it a large array of random floats and checks if it sorts them correctly.
def test_sortIndexList(chatbot, rnd_ArrayInt):
    sorted_rnd = chatbot.sortIndexList(rnd_ArrayInt)
    for i in range(0,len(sorted_rnd) - 2):
        if sorted_rnd[i] > sorted_rnd[i+1]:
            p = True
        else:
            P = False
    assert p

#This test ensure that the bot gives a response of any kind when given a user input
#but doesn't test for the context of the response
def test_botResponse(chatbot):
        r = chatbot.botResponse("I am stressed")
        if len(r) > 0:
            assert True
        else:
            assert False
