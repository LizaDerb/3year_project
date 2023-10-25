# 3year_project
Проект Гришановой Анны и Дербеневой Елизаветы: корпус сочинений ЕГЭ. 

## ЧАСТЬ НА 8

Тексты были скачаны с сайта https://mogu-pisat.ru/sochinenie/ege, процесс скачивания отражен в тетрадке **предобработка и морфологический анализ текстов.ipynb**. Данные сохранены в папке /backend/data/: **corpus.json** (метаинформация о текстах), **corpus_sent.json** (к какому тексту относятся предложения), **corpus_tokens.json** (информация о токенах (форма, лемма, POS), к какому предложению относятся). Процесс обработки этих файлов и создания базы данных отражен в **json_to_database.py**. База данных, к которой обращается поиск по корпусу, находится в файле backend/data/**database.db**. 

В backend/**search_functions.py**, backend/**tagset.py**, backend/**search.py** отражены функции типов поиска, используемый тэгсет (pymorphy), главная функция поиска по корпусу соответственно. В тетрадке backend/**testing.ipynb** отражено тестирование разных типов поиска.

## ЧАСТЬ НА 10
