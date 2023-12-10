# preprocessing.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Ensure you have the necessary NLTK data downloaded
# nltk.download('punkt')

def tokenize(text):
    """
    Tokenizes the input text into words.
    
    Args:
    text (str): A string of text to be tokenized.

    Returns:
    list: A list of word tokens.
    """
    return word_tokenize(text)

def stem(words):
    """
    Stems the list of word tokens.
    
    Args:
    words (list): A list of word tokens.

    Returns:
    list: A list of stemmed word tokens.
    """
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in words]

# Example usage
if __name__ == "__main__":
    sample_text = "The runner likes running so he runs every day."
    tokens = tokenize(sample_text)
    stemmed_tokens = stem(tokens)
    print("Original Tokens:", tokens)
    print("Stemmed Tokens:", stemmed_tokens)
