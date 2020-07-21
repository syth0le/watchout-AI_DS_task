import fileinput
import re
from collections import Counter

count = 'words_count.txt'
rez = 'count.txt'

words = (word for line in fileinput.input(count, 'windows-1251')
         for word in re.findall(r'\w+', line.casefold()))

with open('count.txt', 'w') as w:
    for word, count in Counter(words).most_common():
        w.write("{} {},".format(word, count))
