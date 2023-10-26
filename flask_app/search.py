from flask_app.tagset import TAGSET
from flask_app.search_functions import find_from_lemma, find_from_form, find_from_lemma_and_POS, find_from_POS
import re
import pymorphy2

def search(query, bigram=False, trigram=False, previous_token=0):
    morph = pymorphy2.MorphAnalyzer()
    if '%%' in query:
        form = re.search('(?<=%%)[^ ]*(?=%%)', query).group()
        results = find_from_form(form, bigram=bigram, trigram=trigram, previous_token=previous_token)
    elif '+' in query:
        lemma = re.search('[^ ]*(?=\+)', query).group()
        POS = re.search('(?<=\+)[^ ]*', query).group()
        results = find_from_lemma_and_POS(lemma, POS, bigram=bigram, trigram=trigram, previous_token=previous_token)
    elif query in TAGSET:
        POS = query
        results = find_from_POS(POS, bigram=bigram, trigram=trigram, previous_token=previous_token)
    else:
        lemma = morph.parse(query)[0].normal_form
        results = find_from_lemma(lemma, bigram=bigram, trigram=trigram, previous_token=previous_token)
    return results

def pretty_result(result):
    token = re.sub("[^А-яё]+", " ", result[0].split('.')[0].replace('ё', 'е')).strip(' ')
    words = []
    for word in re.sub("[^А-яё]+", " ", result[1][0]).split():
        in_word = re.search('[А-яё]+', word)
        if in_word != None:
            in_word = in_word.group()
            if in_word.lower().replace('ё', 'е') == token:
                words.append(f'<>{token}<>')
            else:
                words.append(word)
        else:
            words.append(word)
    sentence = (' '.join(words)).split('<>')
    sent_1 = sentence[0]
    try:
        sent_token = sentence[1]
    except IndexError:
        sent_token = None
    try:
        sent_2 = sentence[2]
    except IndexError:
        sent_2 = None
    name = result[1][1]
    author = result[1][2]
    link = result[1][3]
    info = ' '.join([name, author])
    return [sent_1, sent_token, sent_2, token, info, link]

def print_result(results, queries):
    text = []
    query = queries
    for result in results:
        res = pretty_result(result)
        text.append(res)
    return [text, query]

def print_result_extra(results, queries):
    text = []
    query = queries
    for result in results:
        token = result[0] + '   '
        sent = result[1][0]
        name = result[1][1]
        author = result[1][2]
        link = result[1][3]
        info = ' '.join([name, author])
        text.append(['', token, sent, '', info, link])
    return [text, query]

def get_results(queries):
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
    if len(queries.split(' ')) > 1:
        return print_result_extra(results, queries)
    else:
        return print_result(results, queries)