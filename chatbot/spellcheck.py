
from nltk.stem import PorterStemmer
import nltk

class SpellCheck():



    ps = PorterStemmer()

    def errorHandlingArray(self, array):


        if " " in array[0]:
            x = []
            z=[]
            for i in range(0,len(array)):
                x = nltk.word_tokenize(array[i])
                y=""
                for w in x:
                    y = y +(self.ps.stem(w)) + " "
                z.append(y)
            return z
        else:
            z = []
            for w in array:
                z.append(self.ps.stem(w))
            return z
