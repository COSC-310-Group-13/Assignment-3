import pytest
import unittest
import chatbot.chatbot as cb
import sys
import os

@pytest.fixture
def chatbot():
    chatbot = cb()
    return chatbot

@pytest.fixture
def userHellos():
    userHellos = ['hello', "what's up", 'hey', 'hi', 'hello', 'howdy', 'sup', 'hey there']
    return userHellos

@pytest.fixture
def boHellos():
    botHellos = ['Hello', 'Good day', 'Hey!', 'Hi!', 'Nice to meet you!', 'Hello there!']
    return botHellos

def test_getQoutes():

    assert True

def test_helloMessage():

    assert True

def test_sortIndexList():

    assert True

def test_botResponse():

    assert True
