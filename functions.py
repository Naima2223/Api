import re
import time
import bs4
from bs4 import BeautifulSoup 
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords 

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
stops = set(stopwords.words("english")) 

def review_to_tockens( raw_review ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    #review_text = BeautifulSoup(raw_review).get_text() 
    #review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    review_text  = ' '.join([elem.text for elem in BeautifulSoup(raw_review, 'html.parser')])
   # print(raw_review)
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower()#.split()   
    words = word_tokenize(words)   
    #
    # 4. Stem all the words
    stemmer = SnowballStemmer(language='english')

    words = [stemmer.stem(word) for word in words]                    
    #
    # 5. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
                 
    # 
    # 6. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 7. Join the words back into one string separated by space, 
    # and return the result.
   # return( " ".join( meaningful_words )) 
    return(meaningful_words)