import pytest
from chatbot.spellcheck import SpellCheck

#loads in the spellcheck class
@pytest.fixture
def spellcheck():
    sc = SpellCheck()
    return sc

#tests the spellcheck functionality by chcking if it can rercognize an appropriate mistake
def test_errorHandlingArray(spellcheck):
    userHellos = ['hello', "what's up", 'hey', 'hi', 'hello', 'howdy', 'sup', 'hey there']
    helloError = spellcheck.errorHandlingArray(userHellos)

    for word in "helloing".split():
        if ((spellcheck.errorHandlingArray(word)) in helloError):
            assert True
        else:
            assert False
