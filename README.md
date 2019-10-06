# Amazon_Reviews_NLP_Project

Contributors: Kristina Barounis & Gal Gilor

## Intro 

This project utilizes natural language processing techniques and algorithms and a dataset of customer reviews from Amazon's electronic products department to answer the following two questions:

1. Do written reviews of Amazon Products align with their associated ratings?
2. What are the most discussed topics in these reviews?

- [Tech Stack](#tech-stack)

- [Process](#process)

- [Data and EDA](#data-and-eda)
    
- [Part 1: Supervised](#part-1-supervised-models)

- [Part 2: Unsupervised](#part-2-unsupervised-models)

- [Future Improvements](#future-improvements)

## Tech Stack

- Python libraries
    - Pandas
    - NLTK
    - Gensim
    - Scikit-learn
    - Matplotlib
    - Seaborn

## Process

For this project, we used a Stanford dataset of Amazon product reviews spanning 18 years. We cleaned the data using standard NLP techniques (i.e. removing stop words, lemmatizing, and tokenizing). We then used supervised classification algorithms to classify reviews into rating buckets (1-5). We also used an unsupervised topic modeling algorithm (LDA) to cluster reviews into topics.
  
## Data and EDA

The original dataset contained 1.7 million reviews on electronic products sold on Amazon. We dropped 1.2 million to reduce class imbalance across rating buckets, ultimately resulting in ~502,000 observations.

![](/Images/class_imbalance.png) ![](/Images/class_imbalance_fixed.png)

We also engineered a number of features:
- number of words in a review
- number of exclamation points used in a review
- number of question markers used in a review

As part of our exploration, we looked at the most common words and bigrams in our corpus. Many of the most common words ultimately get removed as stop words or through our vectorization strategy in which we require words to appear in less than 50% of the documents. Interestingly, many of the most common bigrams ultimately end up as key componenets of different topics produced through unsupervised topic modeling.

![](/Images/Most_common_words.png) ![](/Images/Most_common_bigrams.png) 

We completed a number of pre-processing and data cleaning steps including removing punctuation and stop words, making all letters lowercase, and lemmatizing words. Each of these steps was performed so that words could be grouped together based on their lemma and weren't treated as individual words.

## Part 1: Supervised models

In this readme, we only discuss our initial and final models. For a look at the additional models we created, please see the python notebook titled Supervised_Models.

1. Dummy Classifier:
- The Dummy Classifier, which ______, acheieved an accuracy score of 20%. Given the distribution of our data into 5 rating categories, this makes sense. 

2. Multinomial Naive Bayes
- We were able to achieve a 47% accuracy score Multinomial Naive Bayes 
- We used NLTK's TF-IDF vectorizer with the following parameters: 
    - max_features: 10,000
    - min_df: 2 documents
    - max_df: 50% of documents

## Part 2: Unsupervised models

- Topic Modeling with LDA

## Future Improvements

1. Optimize text cleaning process
    - Given this was our first time working with NLP techniques, we did not create an optimal pipeline for NLP pre-processing. We tokenized and lemmatized our text before realizing that NLTK's vectorizers took in a corpus of documents as is and performed the tokenization step.
    
2. Use topics derived from LDA in supervised classification algorithms
    - We would have liked to use the topics derived from the unsupervised learning algorithm, LDA, in a supervised classification algorithm to determine if we could...
    
3.      
