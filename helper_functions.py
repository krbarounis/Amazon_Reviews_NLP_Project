import matplotlib.pyplot as plt

def clean_review(review):
    """
    clean_review(review):
    Returns the text of a review without puncuation and capital letters
    Params:
        review: individual review from Amazon Product Review dataset
    Returns:
        a review with only lowercase letters and with puncuation removed
    """
    clean = []
    joined_clean_review = ''
    # for each element in the review
    for x in review:
        # if the element is a punctuation, replace it with a space
        if x in string.punctuation:
            x = x.replace(x, " ")
        # otherwise turn the letter into its lowercase form    
        elif x not in string.punctuation:
            x = x.lower()
        # append the letter to the empty list
        clean.append(x)    
        # join the letters into words
        joined_clean_review = "".join(clean)

    return joined_clean_review

def get_tokens(clean_review):
    
    """ 
    get_tokens(clean_review):
    Returns a list of the individual from a review
    Params:
        clean_review: a review that has been wiped of its puncuation and capital letters
    Returns:
        a list of words, excluding "stop words", that comprise a review
    """
    
    #  tokenize & remove stop words
    list_of_tokens = [x for x in word_tokenize(clean_review) if x not in final_stopwords]
    
    # return list of text from each review
    return list_of_tokens


def lem_words(list_of_tokens,lemmatizer):
    """
    lem_words(list_of_tokens, lemmatizer):
    Returns the lemmas of each token
    Params:
        list_of_tokens: list of words (tokens) from a single review
        lemmatizer: instance of the NLTK lemmatizer class
    Returns:
        a string of lemmas that comprise a review
    """
    wrd_list = [lemmatizer.lemmatize(word) for word in list_of_tokens]
    # join the individual lemmas into a single string
    return " ".join(wrd_list)

def finalize_token(reviews):
    """
    finalize_token(reviews):
    Returns the final corpus of reviews
    Params:
        reviews: reviews that have been cleaned
    Returns:
        A list where each element of the list is a string representing a "cleaned" review
    """
    corpus = []
    for review in tqdm(reviews):
        clean = clean_review(review)
        tokens = get_tokens(clean)
        lemmas = lem_words(tokens,lemmatizer)
        corpus.append(lemmas)
    return corpus

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    plot_confusion_matrix(cm, classes,normalize=False,
                          title='Confusion matrix',cmap=plt.cm.Blues)
    
    """
    #Add Normalization Option
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)
    plt.yticks(tick_marks, classes)

    fmt = '.2f'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('confusion')
    
def plot_AUC_ROC(y_score,fpr,tpr):
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    print('AUC: {}'.format(auc(fpr, tpr)))
    plt.figure(figsize=(10,8))
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.yticks([i/20.0 for i in range(21)])
    plt.xticks([i/20.0 for i in range(21)])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()