import pytest
from chatbot.sentiment import classify

#Tests the trained sentiment model by giving a positive statement and seeing if the model
#classifies it correctly.

def test_classify():
    s = classify('I\'m happy for you and your people')
    if s == 'Positive':
        assert True
    else:
        assert False