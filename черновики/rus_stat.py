import pandas as pd

stat_file = "rus_stat.csv"
i = 0

df = pd.read_csv("lenta-ru-news.csv", low_memory=False)
texts = df["text"].tail(10)

with open(stat_file, 'w') as f:
    for line in f:
        text = f.readline()
        f.write(text + "\n")
    """f.write('key' + '\n')
    for text in texts:
        string = str(text) + ";"
        f.write(string + '\n')"""
