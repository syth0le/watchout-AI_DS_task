import fileinput
import re
from collections import Counter
import codecs

d = 'words_count.txt'
test = 'copy_final.txt'

words = (word for line in fileinput.input(test, 'windows-1251')
         for word in re.findall(r'\w+', line.casefold()))
#f = codecs.open('count.txt', encoding='utf-8', mode='w')
with open('count.txt', 'w') as w:
    for word, count in Counter(words).most_common():
        w.write("{} {},".format(word, count))
