# Assignment 3 - An Interactive Conversational Agent

This Project was developed by Sebi Unipan, Chinmay Gopal, Iwan Levin, Amritpal Aujla and Ali Ibrahim.
## Description

This Project aims to impersonate a psychiatrist in the form of an online chat-bot. More specifically, this online chat-bot needs to be able to offer real world advice and be able to hold a conversation with a real person. Our Chat-bot specializes in helping University students with mental health issues such as depression, loneliness and stress.

Our Team truly believes that anonymous online conversation with an intelligent chat-bot can aleviate mental stresses without the added expenses a real psychiatrist would require.

This conversational bot was developed entirely in Python using the Natural Language Processing library, Natural Language Toolkit(NLTK).

The program is made up of two classes: chatbot and main
>chatbot is the class that can has all the attributes of the chat bot and its methods

>main class is where a chatbot object gets created and is run to extract quotes from file as  
>well as running a loop to continuously ask the user for input with a loop in the class until  
>they enter an exit word  

## Installation

To be able to run the chat bot, you need the nltk and sklearn Python packages.
Open up command prompt and type the following:  

`pip install nltk`  

`pip install -U scikit-learn` 

You should then open up a Python interactive console (IDLE) and download all nltk packages by:

`import nltk`
`nltk.download()`

A GUI should pop up, select 'all | All packages' and press download, afterwards close the GUI.

Afterwards, you may run the Main.py file and the bot should work accordingly.

New features:

POS tagging: Using nltk's POS tagging based on stanford's toolkit, this feature takes a word and finds similar words based on context and grammar.
Some words just aren't available in the prewritten text for the chatbot's replies. This feature allows for words that aren't in the replies but are close enough to some aspect that the chatbot can reply to, so the chatbot assumes the user was talking about the new converted word and replies accordingly.

Example:
You: crazy
Calm Bot: Solution: if you are feeling sad, do something that makes you happy.

The word "crazy" is not available in our text file, but since it is close to the words sad and mad, the bot had a response for these similar words and was able to answer.

Spell check: Using PorterStemmer, simple spelling mistakes such as typing "anxieti" instead of "anxiety" can be corrected by removing suffixes from both the response and the reply when checking for similarities. This way a large number of spelling mistakes that involve the end of the word being mispelt or grammatically incorrect can be caught and replied to properly.

Example:
You: depressioning
Calm Bot: Depression can sometimes be overwhelming, just know that you are not alone.

It recognized the depressioning is the same as depression and responded correctly.
