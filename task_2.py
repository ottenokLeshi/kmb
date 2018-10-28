from nltk import word_tokenize
import re

f = open(path_to_file, 'r')
w_words = open(path_to_file, 'w')
w_years = open(path_to_file, 'w')

wordsSet = set()
yearSet = set()

for line in f:
    words = word_tokenize(line.lower())
    for word in words:
        if re.fullmatch('\d+', word):
            if word.__len__() == 4:
                yearSet.add(int(word))
        elif re.match('^\w*$', word):
            wordsSet.add(word)

yearsArr = list(yearSet)
yearsArr.sort()

for year in yearsArr:
    w_years.write(str(year) + "\n")

for word in wordsSet:
    w_words.write(word + "\n")
