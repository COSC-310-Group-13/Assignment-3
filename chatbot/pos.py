import nltk.text
import nltk.corpus
import nltk
import random
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')

class POS():

    out = nltk.text.ContextIndex([word.lower( ) for word in nltk.corpus.brown.words( )])

    def outputExtra(self,sentence):

            array = nltk.word_tokenize(sentence) #converts sentence to array

            newResponse = " "

            x = [" "]

            for i in range(0,len(array)): #choose a random collection of words that is closest to the sentence
                if len(self.out.similar_words(array[i])) != 0:
                    x.append(self.out.similar_words(array[i]))
                    newResponse = newResponse + x[i][random.choice(range(0,len(x[i])))] + " "


            return newResponse
