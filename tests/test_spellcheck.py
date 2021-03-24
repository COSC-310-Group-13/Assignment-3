import pytest
from chatbot.chatbot import ChatBot as cb
from chatbot.spellcheck import SpellCheck

@pytest.fixture
def spellcheck():
    sp = SpellCheck()
    return sp

def test_errorHandlingArray(spellcheck):
    
    assert True
