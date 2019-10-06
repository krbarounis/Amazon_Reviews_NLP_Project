# Amazon_Reviews_NLP_Project

Contributors: Kristina Barounis & Gal Gilor

## Intro 

This project aims to utilize natural language processing algorithms to answer the following two questions about a dataset of reviews on Amazon electronic products:

1. Do written reviews of Amazon Products align with their associated ratings?

2. What are the most discussed topics in these reviews?

- [Tech Stack](#tech-stack)

- [Process](#process)

- [Data and EDA](#data-and-eda)

    - [Cleaning](#cleaning)

    - [Observations](#observations)

    - [Features](#features)
    
    - [Visuals](#visuals)
    
- [Part 1: Supervised](#supervised-models)

- [Part 2: Unsupervised](#unsupervised-models)

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

![](/Images/class_imbalance.png)

![](/Images/class_imbalance_fixed.png)

### NLP Pre-Processing

1. Removed puncuation
2. Made all letters lowercase
3. Removed stopwords 
4. Lemmatized

### EDA

Top words in corpus, top bigrams in corpus


## Part 1: Supervised models

Only covers initial and final models. For additional models run, see python notebook: Supervised Models.

1. Dummy Classifier
- 20% accuracy given distribution of data into 5 rating groups

2. Multinomial Naive Bayes
- 47% accuracy

## Part 2: Unsupervised models

- Topic Modeling with LDA


## Future Improvements

1. Optimize text cleaning process:
    - Given this was our first time working with NLP techniques
2. Use topics as classifiers
    - 
3.      
