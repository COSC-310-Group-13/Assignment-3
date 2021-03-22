import pytest
import unittest
from chatbot.chatbot import ChatBot as cb
import math
import random

@pytest.fixture
def chatbot():
    chatbot = cb()
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
    rndint = {}
    for i in range(0,1000):
        rnd = random.randfloat(0,100)
        math.round(rnd)
        rndint.append(rnd)
    
    return rndint

def test_getQoutes():

    assert True

def test_helloMessage(chatbot, userHellos, botHellos):
    p = False  
    for i in range(0,len(userHellos)-1):
        if chatbot.helloMessage(userHellos[i]) in botHellos:
            p = True
        else:
            p = False

    assert p

def test_sortIndexList():

    assert True

def test_botResponse():

    assert True
