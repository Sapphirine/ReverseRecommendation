import nltk
import os
import string

from nltk.tokenize import TweetTokenizer
from stop_words    import get_stop_words

doc_dir = os.path.join(os.path.dirname(__file__), "doc")
keyword_general_path = os.path.join(doc_dir, 'keyword_map_general.txt')
keyword_special_path = os.path.join(doc_dir, 'keyword_map_special.txt')


def keywords_search(reviews):
    key_map = {}

    for k in open(keyword_general_path, 'r'):
        a = k.strip().split(", ")
        key_map[a[0]] = a[1]

    special_map = {}

    for k in open(keyword_special_path, 'r'):
        a = k.strip().split(", ")
        special_map[a[0]] = a[1]

    # get the tokens from the review
    raw = reviews.lower()
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(raw)

    # remove punctuations
    no_punc_tokens = [i for i in tokens if (not i in string.punctuation + string.digits) and (not "." in i)]

    # remove stop words from tokens
    en_stop = get_stop_words('en')
    stopped_tokens = [i for i in no_punc_tokens if not i in en_stop]

    chosen_key_words = ['chinese']

    # Search in general key word
    key_words_dict = dict.fromkeys(key_map.values(), 0)

    # Select keyword use only key word to select
    s = set(stopped_tokens)
    for t in key_map.keys():
        if t in s:
            key_words_dict[key_map[t]] += 1

    for d in sorted(zip(key_words_dict.values(), key_words_dict.keys()))[:-4:-1]:
        if d[0] > 0:
            chosen_key_words.append(d[1])

    # Search in special keyword
    special_words_dict = dict.fromkeys(special_map.values(), 0)
    #  Select keyword using wordnet

    # Select keyword use only key word to select
    s = set(stopped_tokens)
    for t in special_map.keys():
        if t in s:
            special_words_dict[special_map[t]] += 1

    for d in sorted(zip(special_words_dict.values(), special_words_dict.keys()))[:-3:-1]:
        if d[0] > 0:
            chosen_key_words.append(d[1])

    return ', '.join(chosen_key_words)

if __name__ == "__main__":
    infile = open("doc/test_review.txt", 'r')
    print keywords_search(infile.read())
