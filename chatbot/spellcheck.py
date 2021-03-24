
from nltk.stem import PorterStemmer
import nltk

class SpellCheck():

    ps = PorterStemmer()

    def errorHandlingArray(self, array): #this method removes suffixes to correct for some errors


        if " " in array[0]:              #for arrays with sentences
            curr = []
            newArray =[]
            for i in range(0,len(array)):
                curr = nltk.word_tokenize(array[i])  #takes array[i] and puts it in a temporary variable
                y=""    #makes y empty each iteration of i
                for w in curr:
                    y = y +(self.ps.stem(w)) + " "       #concatenates the words in curr after they have been stemmed
                newArray.append(y)                       #newArray contains all the sentences after they have been stemmed
            return newArray
        elif isinstance(array,list):                       #for arrays with just words
            newArray = []
            for w in array:
                newArray.append(self.ps.stem(w))
            return newArray
        else:
            newArray = self.ps.stem(array)
            return newArray
