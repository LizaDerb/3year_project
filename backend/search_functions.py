def find_from_lemma(lemma, cur, bigram=False, trigram=False, previous_token=0):
    if bigram:
        bigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        bigram_command = ''
    if trigram:
        trigram_command = f""" AND corpus_tokens.token_id = {previous_token+2}"""
    else:
        trigram_command = ''
    command = f"""
SELECT corpus_tokens.token_id, corpus_tokens.token, corpus_sent.sent_text, corpus.doc_name, corpus.author, corpus.doc_link
FROM corpus_lemma
    INNER JOIN corpus_tokens ON corpus_tokens.token_id = corpus_lemma.token_id
	INNER JOIN corpus_sent ON corpus_sent.sent_id = corpus_tokens.sent_id
	INNER JOIN corpus ON corpus.doc_id = corpus_sent.doc_id
WHERE corpus_lemma.lemma = "{lemma}"{bigram_command}{trigram_command}
"""
    cur.execute(command)
    finds = cur.fetchall()
    return finds


def find_from_form(form,cur, bigram=False, trigram=False, previous_token=0):
    if bigram:
        bigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        bigram_command = ''
    if trigram:
        trigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        trigram_command = ''
    command = f"""
SELECT corpus_tokens.token_id, corpus_tokens.token, corpus_sent.sent_text, corpus.doc_name, corpus.author, corpus.doc_link
FROM corpus_tokens
	INNER JOIN corpus_sent ON corpus_sent.sent_id = corpus_tokens.sent_id
	INNER JOIN corpus ON corpus.doc_id = corpus_sent.doc_id
WHERE corpus_tokens.token = "{form}"{bigram_command}{trigram_command}
"""
    cur.execute(command)
    finds = cur.fetchall()
    return finds


def find_from_lemma_and_POS(lemma, POS, cur, bigram=False, trigram=False, previous_token=0):
    if bigram:
        bigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        bigram_command = ''
    if trigram:
        trigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        trigram_command = ''
    command = f"""
SELECT corpus_tokens.token_id, corpus_tokens.token, corpus_sent.sent_text, corpus.doc_name, corpus.author, corpus.doc_link
FROM corpus_lemma
    INNER JOIN corpus_tokens ON corpus_tokens.token_id = corpus_lemma.token_id
	INNER JOIN corpus_POS ON corpus_POS.token_id = corpus_lemma.token_id
	INNER JOIN corpus_sent ON corpus_sent.sent_id = corpus_tokens.sent_id
	INNER JOIN corpus ON corpus.doc_id = corpus_sent.doc_id
WHERE corpus_lemma.lemma = "{lemma}" AND corpus_POS.POS = "{POS}"{bigram_command}{trigram_command}
"""
    cur.execute(command)
    finds = cur.fetchall()
    return finds


def find_from_POS(POS, cur, bigram=False, trigram=False, previous_token=0):
    if bigram:
        bigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        bigram_command = ''
    if trigram:
        trigram_command = f""" AND corpus_tokens.token_id = {previous_token+1}"""
    else:
        trigram_command = ''
    command = f"""
SELECT corpus_tokens.token_id, corpus_tokens.token, corpus_sent.sent_text, corpus.doc_name, corpus.author, corpus.doc_link
FROM corpus_POS
    INNER JOIN corpus_tokens ON corpus_tokens.token_id = corpus_POS.token_id
	INNER JOIN corpus_sent ON corpus_sent.sent_id = corpus_tokens.sent_id
	INNER JOIN corpus ON corpus.doc_id = corpus_sent.doc_id
WHERE corpus_POS.POS = "{POS}"{bigram_command}{trigram_command}
"""
    cur.execute(command)
    finds = cur.fetchall()
    return finds