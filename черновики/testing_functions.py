import codecs
import re
from typing import Any

import pymorphy2
from nltk.corpus import stopwords
import time
from collections import Counter

morph = pymorphy2.MorphAnalyzer()
rus_stopwords = stopwords.words("russian")
rus_stopwords.append('')

stat_file = 'test_data_rus.txt'
lenta = 'lenta-ru-news.csv'


n = time.time()
f = codecs.open('zhopa.txt', "r", "utf_8_sig")
reg = re.compile('[^а-яА-Яa-zA-Z]')
i = 0

with open('temptig.txt', 'a') as w:
    for line in f.readlines():
        list_of_lists = line.replace(',', ' ').split(' ')
        i += 1
        print(i, end=',')
        #c = Counter([morph.parse(reg.sub('', word).lower().strip())[0].normal_form for word in list_of_lists])
        #w.write(str("{}|{}\n".format(c.keys(), c.values())))
        for word in list_of_lists:
            w.write(str(reg.sub('', word).lower().strip())+' ')
        #f.write(str([reg.sub('', word).lower().strip() for word in list_of_lists]) + "\n")


m = time.time()
f.close()

print("\n{}".format(m - n))
