import string
from nltk import PorterStemmer, corpus
from nltk.tokenize import word_tokenize
from nltk import tokenize
from unidecode import unidecode

def pre_processing():
    foo_words = corpus.stopwords.words("portuguese")
    token_space = tokenize.WhitespaceTokenizer()
    return foo_words, token_space

def split_phrase(foo_words, token_space, msg):
    new_phrase = []
    list_new_phrase = []
    words_text = token_space.tokenize(msg.lower())
    for words in words_text:
        if (words not in foo_words):
            new_phrase.append(words)     
    list_new_phrase.append(' '.join(new_phrase))
    return new_phrase, list_new_phrase

def no_punctuation(phrase):
    tokens = word_tokenize(phrase)
    tokens_no_ponctuation = [token for token in tokens if token not in string.punctuation]
    phrase_no_ponctuation = ' '.join(tokens_no_ponctuation)
    return phrase_no_ponctuation

def no_accent(phrase):
    tokens = word_tokenize(phrase)
    tokens_no_ponctuation = [unidecode(token) for token in tokens]
    phrase_no_ponctuation = ' '.join(tokens_no_ponctuation)
    return phrase_no_ponctuation

def stream_done(phrase):
    stemmer = PorterStemmer()
    tokens = word_tokenize(phrase)
    stems = [stemmer.stem(token) for token in tokens]
    return ' '.join(stems)

def processing(msg):
    foo_words, token_space = pre_processing()
    msg = no_punctuation(msg)
    msg = no_accent(msg)
    msg = stream_done(msg)
    return split_phrase(foo_words, token_space, msg)

    