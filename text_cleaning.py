import pandas as pd
import json
import string
import nltk
from nltk.corpus import stopwords
from  nltk import FreqDist, word_tokenize 
from nltk.stem import WordNetLemmatizer
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import seaborn as sns
import matplotlib.pyplot as plt


def clean_review(review):
    ''' This functions receives a document, removes punctuation, and lower cases the characters '''
    clean = []
    joined_clean_review = ''
    for x in review:
        if x in string.punctuation:
            x = x.replace(x, " ")
        elif x not in string.punctuation:
            x = x.lower()
        clean.append(x)    
        joined_clean_review = "".join(clean)

    return joined_clean_review


def get_tokens(clean_review):
    ''' This function receives a document, removes stop words, and tokenizes the documents '''  
    #  tokenize & remove stop words
    list_of_tokens = [x for x in word_tokenize(clean_review) if x not in final_stopwords]
    
    # return list of text from each review
    return list_of_tokens