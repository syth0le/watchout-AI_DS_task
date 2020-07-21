import codecs
import re
import pymorphy2
from nltk.corpus import stopwords
import time

""" Creating class instance of MorphAnalyzer. Connect all work files and announce stopwords."""
morph = pymorphy2.MorphAnalyzer()
rus_stopwords = stopwords.words("russian")
rus_stopwords.append('')
rus_stopwords.append('по')
rus_stopwords.append('с')

stat_file = 'test_data_rus.txt'
lenta = 'lenta-ru-news.csv'
count = 'words_count.txt'

""" Creating expression mask."""
n = time.time()
i = 0
reg = re.compile('[^а-яА-Яa-zA-Z]')

""" Open file and read it line by line. 
process all the lines and get words in an undefined form at the output """

f = codecs.open(lenta, encoding='utf-8', mode='r')
for line in f.readlines():
    list_of_lists = line.replace(',', ' ').replace('-', ' ').split(' ')
    with open(count, 'a') as w:
        for word in list_of_lists:
            if word not in rus_stopwords:
                w.write(morph.parse(reg.sub('', word))[0].normal_form + ' ')
        w.write('\n')
    i += 1
    print(i, end=',')

m = time.time()
f.close()

print("\n{}".format(m - n))  # count work time
