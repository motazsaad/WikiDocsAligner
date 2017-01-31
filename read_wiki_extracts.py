from bs4 import BeautifulSoup
import os
import parse_sql_script



'''
arz:
SELECT * FROM ar_langlinks
where ar_langlinks.ll_lang = 'arz' and ar_langlinks.ll_title = 'ميه'
;

'7', 'arz', 'ميه'


ar:
SELECT * FROM arz_langlinks
where arz_langlinks.ll_lang = 'ar' and arz_langlinks.ll_title = 'ماء'
;
'35097', 'ar', 'ماء'





'''



#wiki_file = "/home/motaz/Downloads/wiki/arwiki/AA/wiki_00"


def load_corpus(corpus_dir):
    corpus = list()
    for subdir, dirs, files in os.walk(corpus_dir):
        for f in files:
            wiki_file = os.path.join(subdir, f)
            with open(wiki_file, encoding='utf-8') as wiki_reader:
                text = wiki_reader.read()
                soup = BeautifulSoup(text, 'html.parser')
                docs = soup.find_all('doc')
                for doc in docs:
                    doc_id = doc.get('id')
                    title = doc.get('title')
                    corpus.append((doc_id, title, doc))
    return corpus


def getTargetTitle(df, doc_id, ll_lang):
    return df.loc[(df.ll_from == doc_id) & (df.ll_lang == ll_lang), 'll_title'].values[0]



def align_corpus(src_corpus, target_corpus):
    arz_df, ar_df = parse_sql_script.load_df()
    for wiki_doc in src_corpus:
        doc_id, title, doc = wiki_doc
        target_title = getTargetTitle(ar_df, doc_id, 'arz')











if __name__ == '__main__':
    src_corpus_dir = '/home/motaz/Downloads/wiki/arzwiki/'
    target_corpus_dir = '/home/motaz/Downloads/wiki/arwiki/'

    src_corpus = load_corpus(src_corpus_dir)
    target_corpus = load_corpus(target_corpus_dir)

