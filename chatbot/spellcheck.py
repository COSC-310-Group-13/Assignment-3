
from nltk.stem import PorterStemmer
import nltk

class SpellCheck():



    ps = PorterStemmer()

    def errorHandlingArray(self, array):


        if " " in array[0]:
            curr = []
            newArray =[]
            for i in range(0,len(array)):
                curr = nltk.word_tokenize(array[i])
                y=""
                for w in curr:
                    y = y +(self.ps.stem(w)) + " "
                newArray.append(y)
            return newArray
        else:
            newArray = []
            for w in array:
                newArray.append(self.ps.stem(w))
            return newArray
