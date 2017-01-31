from bs4 import BeautifulSoup
import os
import parse_sql_script


#wiki_file = "/home/motaz/Downloads/wiki/arwiki/AA/wiki_00"



def load_corpus(corpus_dir):
    corpus = list()
    for subdir, dirs, files in os.walk(corpus_dir):
        for f in files:
            wiki_file = os.path.join(subdir, f)
            with open(wiki_file, encoding='utf-8') as wiki_reader:
                text = wiki_reader.read()
                soup = BeautifulSoup(wiki_file, 'html.parser')
                docs = soup.find_all('doc')
                for doc in docs:
                    doc_id = doc.get('id')
                    title = doc.get('title')
                    corpus.append((doc_id, title, doc))


def align_corpus(src_corpus, target_corpus):
    arz_df, ar_df = parse_sql_script.load_df()
    for wiki_doc in src_corpus:
        doc_id, title, doc = wiki_doc









if __name__ == '__main__':
    src_corpus_dir = '/home/motaz/Downloads/wiki/arzwiki/'
    target_corpus_dir = '/home/motaz/Downloads/wiki/arwiki/'

    src_corpus = load_corpus(src_corpus_dir)
    target_corpus = load_corpus(target_corpus_dir)

