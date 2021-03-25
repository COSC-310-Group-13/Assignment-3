import pytest
from chatbot.spellcheck import SpellCheck

@pytest.fixture
def spellcheck():
    sc = SpellCheck()
    return sc


def test_errorHandlingArray(spellcheck):
    userHellos = ['hello', "what's up", 'hey', 'hi', 'hello', 'howdy', 'sup', 'hey there']
    helloError = spellcheck.errorHandlingArray(userHellos)

    for word in "helwo".split():
        if ((spellcheck.errorHandlingArray(word)) in helloError):
            assert True
        else:
            assert False
