from tagset import TAGSET
from search_functions import find_from_lemma, find_from_form, find_from_lemma_and_POS, find_from_POS
import re
import sqlite3
import pymorphy2

#con = sqlite3.connect('data/database.db')  # подключение
#cur = con.cursor()  # курсор
#queries = input('Введите запрос: ')
def search(query, bigram=False, trigram=False, previous_token=0):
    morph = pymorphy2.MorphAnalyzer()
    if '%%' in query:
        form = re.search('(?<=%%)[^ ]*(?=%%)', query).group()
        results = find_from_form(form, cur, bigram=bigram, trigram=trigram, previous_token=previous_token)
    elif '+' in query:
        lemma = re.search('[^ ]*(?=\+)', query).group()
        POS = re.search('(?<=\+)[^ ]*', query).group()
        results = find_from_lemma_and_POS(lemma, POS, cur, bigram=bigram, trigram=trigram, previous_token=previous_token)
    elif query in TAGSET:
        POS = query
        results = find_from_POS(POS, cur, bigram=bigram, trigram=trigram, previous_token=previous_token)
    else:
        lemma = morph.parse(query)[0].normal_form
        results = find_from_lemma(lemma, cur, bigram=bigram, trigram=trigram, previous_token=previous_token)
    return results

def print_result(results):
    for result in results:
        print(result[0], result[1][0],
             result[1][1], result[1][2], result[1][3], sep='\n')
        print('\n')
def get_results(cur, queries):
    queries = queries.replace('"','%%')
    results = []
    for find_0 in search(queries.split()[0]):
        if len(queries.split()) == 1:
            results.append([f'{find_0[1]}', find_0[2:]])
        else:
            previous_token_0 = int(find_0[0])
            for find_1 in search(queries.split()[1], bigram=True, previous_token=previous_token_0):
                if len(queries.split()) == 3:
                    previous_token_1 = int(find_1[0])
                    for find_2 in search(queries.split()[2], trigram=True, previous_token=previous_token_1):
                        if previous_token_1 == previous_token_0 + 1:
                            results.append([f'{find_0[1]} {find_1[1]} {find_2[1]}', find_0[2:]])
                else:
                    results.append([f'{find_0[1]} {find_1[1]}', find_0[2:]])
    return results
