from stop_words import get_stop_words
from nltk import word_tokenize
from collections import Counter
import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()
f = open(path_to_file, 'r')
w = open(path_to_file, 'w')
text = f.read()

stop_words = get_stop_words('russian')
stop_words.append("автор")
stop_words.append("дата")

words = word_tokenize(text.lower())


def remove_stop_and_chars(string):
    if string in stop_words \
            or re.match("автор", string) \
            or re.match("дата", string) \
            or not re.match('^\w+$', string) \
            or re.match('_{16}', string):
        return False
    else:
        return True


words = list(filter(remove_stop_and_chars, words))

words = [morph.normal_forms(word)[0] for word in words]
counter = Counter(words)

print(counter.most_common(30))
