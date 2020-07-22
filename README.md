# Watchout!AI Data Science Task

Данный репозиторий предоставляет ответы на полученные задания от компании Watchout!AI.
Ответы на все теоретические и практические задания представлены в данных файлах:
* [Theory](https://github.com/syth0le/watchout-AI_DS_task/blob/master/answers.txt)
* [1-part(EDA)](https://github.com/syth0le/watchout-AI_DS_task/blob/master/1.EDA.ipynb)
* [2-part(N-grams)](https://github.com/syth0le/watchout-AI_DS_task/blob/master/2.N_Grams.ipynb)

## Description

Структура выполненной работы выглядит следующим образом:

Описательная статистика и все необходимые для нее вычисления выполнены в файле [1-part(EDA)](https://github.com/syth0le/watchout-AI_DS_task/blob/master/1.EDA.ipynb), 
Все необходимые вычисления, связанные с подсчетом и лематизацией слов провел в файлах 
[filtering](https://github.com/syth0le/watchout-AI_DS_task/blob/master/words_refiltering.py) и
[count](https://github.com/syth0le/watchout-AI_DS_task/blob/master/count.py), 
Вынес решение данных подзадач в отдельные файлы, так как ОЗУ и компьютер не справлялся с Jupiter Notebook, 
а запуская с командной строки, все работало без проблем.
выявление наиболее значимых N-грамм представлено в файле [2-part(N-grams)](https://github.com/syth0le/watchout-AI_DS_task/blob/master/2.N_Grams.ipynb)
ну и ответы на теорию можете найти здесь [Theory](https://github.com/syth0le/watchout-AI_DS_task/blob/master/answers.txt).

* Перед проверкой задания, чтобы не ждать работы алгоритма загрузите необходимые файлы с [Яндекс.Диска](https://yadi.sk/d/l01lCltqv2ip2Q).

## How Files Work

После долгих поисков и многочисленных оптимизационных решений пришел к выводу что загружать весь файл в память бессмысленно.
Правильнее читать файл построково и пытаться сделать с каждой строкой как можно больше действий, прежде чем записать
результаты работы с ней в другой временный файл.
Мое решение позволило ускорить работу с таким большим файлом в сотни (если не тысячи) раз.
Чтобы не хранить в памяти такие обьемы данных, и не загружать ОЗУ и процессор под 100%, было принято именно такое решение.

Если вы не хотите ждать какое то время, пока алгоритм сработает, то скачайте временные файлы с данного 
[Яндекс.Диска](https://yadi.sk/d/l01lCltqv2ip2Q). Тут находятся все временные файлы, которые я заранее решил посчитать.

Также для дополнительной информации загружаю в репозиторий [черновики](https://github.com/syth0le/watchout-AI_DS_task/tree/master/%D1%87%D0%B5%D1%80%D0%BD%D0%BE%D0%B2%D0%B8%D0%BA%D0%B8) для полной иллюстрации хода мыслей при решении задания.

## Feedback
U can find me in these social networks:
* [VK](https://vk.com/sythole)
* [LinkedIn](https://www.linkedin.com/in/daniil-cherednichenko-4294141b0/)
* [Instagram](https://www.instagram.com/syth0le/)
*  chdan565@gmail.com


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Copyright (c) [2020] [syth0le]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.