#Libraries needed to install:
# nltk, scikit-learn

#Import libraries
import subprocess
import sys
import random
import string
import nltk
from chatbot.spellcheck import SpellCheck
from chatbot.pos import POS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chatbot import sentiment
from nltk.corpus import wordnet
#nltk.download(quiet = True)


#This the class of the chatbot which reads both positive and negative quotes from a file and places them into
#a list. When the user enters an input, the bot traverses the users' input to check if
#it contains any greeting words. If it does not contain any greeting words, the
#bot scores each quote from the file based on how similar it is to the users'
#input. #The quote that is most similar to the users' input is outputted so that
#quotes match the topic the user talks about.


class ChatBot():

    out = nltk.text.ContextIndex([word.lower( ) for word in nltk.corpus.brown.words( )])

    sc = SpellCheck()
    CV = CountVectorizer()
    posQuotes = []
    negQuotes = [] #lines taken from files will be placed in posQuotes and negQuotes to talk to user
    pos = POS()

    def __init__(self):
        print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!") #initialize the bot

        #extractQuotes function reads the quotes text file and tokenizes them into a list of sentences.

    def extractQuotes(self, fileName):
        if fileName[0] == 'p':
            file = open(fileName, 'r', encoding='utf-8')
            text = file.read()
            file.close()
            self.posQuotes = nltk.sent_tokenize(text) #extract quotes to posQuotes or negQuotes
        elif fileName[0] == 'n':
            file = open(fileName, 'r', encoding='utf-8')
            text = file.read()
            file.close()
            self.negQuotes = nltk.sent_tokenize(text)

    def helloMessage(self, userInput):
        userInput = userInput.lower() #make everything lowercase so bot can doesn't deal with cases

        #ChatBot hello messages
        botHellos = ['Hello', 'Good day', 'Hey!', 'Hi!', 'Nice to meet you!', 'Hello there!']
        #User possible hello messages
        userHellos = ['hello', "what's up", 'hey', 'hi', 'hello', 'howdy', 'sup', 'hey there']


        helloError = self.sc.errorHandlingArray(userHellos)

        for word in userInput.split():
            if ((self.sc.errorHandlingArray(word)) in helloError) :         #correcting for possible errors in the end of the response
                return random.choice(botHellos)

        #The sortIndexList function turns the similarityScoresList from the botResponse function
        #to output the indices of the each quote in decreasing order of similarity
        #to the users' input

    def sortIndexList(self, scoresList):
        length = len(scoresList)
        retList = list(range(0, length))

        for i in range(length):
            for j in range(length):
                if scoresList[retList[i]] > scoresList[retList[j]]:
                    temp = retList[i]
                    retList[i] = retList[j]
                    retList[j] = temp
        return retList


    def botResponse(self, userInput):
        userInput = userInput.lower()   #convert text to lowercase
        reasonableResponse = ["I'm sorry, I didn't quite understand what you just typed.","Sorry I'm not capable talking about that right now.",
                                      "Your choice of discussion is out of my range.", "I didn't get that could you try again?",
                                      "Unfortunealy I don't recognize what your trying to tell me."]
                                      
        potentialAdjectives = ['happy','sad','lazy','tired','angry','lonely','bad','lost', 'hurt']

        for i in range(len(potentialAdjectives)):

            synList = []
            for syn in wordnet.synsets(potentialAdjectives[i]):
                for x in syn.lemmas():
                    synList.append(x.name())

            for k in range(len(synList)):
                if (synList[k] in userInput):
                    userInput = userInput +' '+potentialAdjectives[i]

        sent = sentiment.classify(userInput)
        if sent == "Positive":
            errorResponse = self.sc.errorHandlingArray(userInput)
            self.posQuotes.append(errorResponse) #add users' input to end of posQuotes list
            errorArray = self.sc.errorHandlingArray(self.posQuotes) #error array contains the same content as posQuotes, but corrects for errors

            response = ''      #initialize the bots response
            countArray = self.CV.fit_transform(errorArray)             ##these two lines form the similarity scores between
            similarityScores = cosine_similarity(countArray[-1], countArray)    ##each quote and the users input to output the most similar one
            similarityScoresList = similarityScores.flatten()   #similarityScores is not a 1 dimensional array, so we flatten it
            indexOfQuote = self.sortIndexList(similarityScoresList)  #this gives us the indices of the most similar to least similar quotes
            indexOfQuote = indexOfQuote[1:]     #remove the first element as it is the index of the users' input

            if similarityScoresList[indexOfQuote[0]] != 0.00:       #if there are posQuotes similar to users' input it outputs most similar quote
                self.posQuotes.remove(errorResponse)                       #otherwise, it outputs that it does not understand users' input
                return response + self.posQuotes[indexOfQuote[0]]
            elif similarityScoresList[indexOfQuote[0]] == 0.00:

                self.posQuotes.remove(errorResponse)

                for i in range(0,10):
                    z = self.pos.outputExtra(userInput)      #this loop keeps iterating until a match is found, random sentences are generated each time using POS
                    self.posQuotes.append(z)
                    errorArray = self.sc.errorHandlingArray(self.posQuotes) #error array contains the same content as quotes, but corrects for errors
                    response = ''      #initialize the bots response
                    countArray = self.CV.fit_transform(errorArray)             ##these two lines form the similarity scores between
                    similarityScores = cosine_similarity(countArray[-1], countArray)    ##each quote and the users input to output the most similar one
                    similarityScoresList = similarityScores.flatten()   #similarityScores is not a 1 dimensional array, so we flatten it
                    indexOfQuote = self.sortIndexList(similarityScoresList)  #this gives us the indices of the most similar to least similar quotes
                    indexOfQuote = indexOfQuote[1:]
                    if similarityScoresList[indexOfQuote[0]] != 0.00:       #if there posQuotes similar to users' input it outputs most similar quote
                        self.posQuotes.remove(z)                       #otherwise, it outputs that it does not understand users' input
                        return response + self.posQuotes[indexOfQuote[0]]
                    self.posQuotes.remove(z)
                return response + ' ' + random.choice(reasonableResponse)
        else:
            errorResponse = self.sc.errorHandlingArray(userInput)
            self.negQuotes.append(errorResponse) #add users' input to end of negQuotes list
            errorArray = self.sc.errorHandlingArray(self.negQuotes) #error array contains the same content as negQuotes, but corrects for errors

            response = ''      #initialize the bots response
            countArray = self.CV.fit_transform(errorArray)             ##these two lines form the similarity scores between
            similarityScores = cosine_similarity(countArray[-1], countArray)    ##each quote and the users input to output the most similar one
            similarityScoresList = similarityScores.flatten()   #similarityScores is not a 1 dimensional array, so we flatten it
            indexOfQuote = self.sortIndexList(similarityScoresList)  #this gives us the indices of the most similar to least similar quotes
            indexOfQuote = indexOfQuote[1:]     #remove the first element as it is the index of the users' input

            if similarityScoresList[indexOfQuote[0]] != 0.00:       #if there negQuotes similar to users' input it outputs most similar quote
                self.negQuotes.remove(errorResponse)                       #otherwise, it outputs that it does not understand users' input
                return response + self.negQuotes[indexOfQuote[0]]
            elif similarityScoresList[indexOfQuote[0]] == 0.00:

                self.negQuotes.remove(errorResponse)

                for i in range(0,10):
                    z = self.pos.outputExtra(userInput)      #this loop keeps iterating until a match is found, random sentences are generated each time using POS
                    self.negQuotes.append(z)
                    errorArray = self.sc.errorHandlingArray(self.negQuotes) #error array contains the same content as negQuotes, but corrects for errors
                    response = ''      #initialize the bots response
                    countArray = self.CV.fit_transform(errorArray)             ##these two lines form the similarity scores between
                    similarityScores = cosine_similarity(countArray[-1], countArray)    ##each quote and the users input to output the most similar one
                    similarityScoresList = similarityScores.flatten()   #similarityScores is not a 1 dimensional array, so we flatten it
                    indexOfQuote = self.sortIndexList(similarityScoresList)  #this gives us the indices of the most similar to least similar quotes
                    indexOfQuote = indexOfQuote[1:]
                    if similarityScoresList[indexOfQuote[0]] != 0.00:       #if there negQuotes similar to users' input it outputs most similar quote
                        self.uotes.remove(z)                       #otherwise, it outputs that it does not understand users' input
                        return response + self.negQuotes[indexOfQuote[0]]
                    self.negQuotes.remove(z)
                return response + ' ' + random.choice(reasonableResponse)

