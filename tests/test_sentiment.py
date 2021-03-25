import pytest
from chatbot.sentiment import classify


def test_classify():
    s = classify('I\'m happy')
    if s == 'Positive':
        assert True
    else:
        assert False