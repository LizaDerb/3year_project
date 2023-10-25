import pandas as pd
import sqlite3
import json

with open('data/corpus.json',encoding='utf-8') as f:
    corpus = json.load(f)
corpus = pd.DataFrame(corpus).transpose().rename(columns={0:'doc_text',
                                                 1: 'doc_name',
                                                 2: 'author',
                                                 3: 'doc_link'})
corpus['doc_id'] = corpus.index

with open('data/corpus_sent.json',encoding='utf-8') as f:
    corpus_sent = json.load(f)
corpus_sent = pd.DataFrame(corpus_sent).transpose().rename(columns={0:'sent_text',
                                                 1: 'doc_id'})
corpus_sent['sent_id'] = corpus_sent.index

with open('data/corpus_tokens.json',encoding='utf-8') as f:
    corpus_tokens = json.load(f)
corpus_tokens = pd.DataFrame(corpus_tokens).transpose().rename(columns={'wordform':'token',
                                                                       'pos': 'POS'})
corpus_tokens['token_id'] = corpus_tokens.index

corpus_POS = corpus_tokens[['token_id','POS']]
corpus_lemma = corpus_tokens[['token_id','lemma']]
corpus_tokens = corpus_tokens[['token_id','token','sent_id']]

con = sqlite3.connect('data/database.db')  # подключение
cur = con.cursor()  # курсор

pd.DataFrame(corpus_tokens).to_sql(name='corpus_tokens', con=con, index=False)
pd.DataFrame(corpus_sent).to_sql(name='corpus_sent', con=con, index=False)
pd.DataFrame(corpus).to_sql(name='corpus', con=con, index=False)
pd.DataFrame(corpus_POS).to_sql(name='corpus_POS', con=con, index=False)
pd.DataFrame(corpus_lemma).to_sql(name='corpus_lemma', con=con, index=False)

con.close()