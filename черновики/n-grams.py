import fileinput
import re
import nltk
from string import punctuation
import codecs
#s = ''.join(c for c in s if c not in punctuation)

d = 'words_count.txt'
test = 'copy_final.txt'
prog = re.compile('[А-Яа-я]+')


reg = re.compile('[^а-яА-Яa-zA-Z]')
f = codecs.open(d, encoding='utf-8', mode='r')
for line in f.readlines():
    list_of_lists = line.replace(',', ' ').replace('-', ' ').split(' ')
    (reg.sub('', word).lower().strip())+' '

d = 'words_count.txt'
test = 'copy_final.txt'
prog = re.compile('[А-Яа-я]+')


words = (word for line in fileinput.input(test, 'windows-1251')
         for word in re.findall(r'\w+', line.casefold()))
bg = list(nltk.bigrams(words))
bgfd = nltk.FreqDist(bg)
print(bgfd.most_common(18))