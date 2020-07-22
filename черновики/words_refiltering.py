import codecs
import re
import pymorphy2
from nltk.corpus import stopwords
import time

morph = pymorphy2.MorphAnalyzer()
rus_stopwords = stopwords.words("russian")
rus_stopwords.append('')
rus_stopwords.append('по')
rus_stopwords.append('с')

stat_file = 'test_data_rus.txt'
lenta = 'lenta-ru-news.csv'
data_file = 'temptig.txt'
datas = 'words_count.txt'

n = time.time()
morph = pymorphy2.MorphAnalyzer()
i = 0
reg = re.compile('[^а-яА-Яa-zA-Z]')

f = codecs.open(lenta, encoding='utf-8', mode='r')
for line in f.readlines():
    list_of_lists = line.replace(',', ' ').replace('-', ' ').split(' ')
    with open(datas, 'a') as w:
        for word in list_of_lists:
            if word not in rus_stopwords:
                w.write(morph.parse(reg.sub('', word))[0].normal_form + ' ')
        w.write('\n')
    i += 1
    print(i)

m = time.time()
f.close()

print("\n{}".format(m - n))
