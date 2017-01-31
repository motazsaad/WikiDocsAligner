from bs4 import BeautifulSoup
import os


#wiki_file = "/home/motaz/Downloads/wiki/arwiki/AA/wiki_00"



def load_corpus(corpus_dir):
    wiki_docs = list()
    for subdir, dirs, files in os.walk(corpus_dir):
        for f in files:
            wiki_file = os.path.join(subdir, f)
            with open(wiki_file, encoding='utf-8') as wiki_reader:
                text = wiki_reader.read()
                wiki_docs.append(text)



def align_docs(wiki_doc):
        soup = BeautifulSoup(wiki_doc, 'html.parser')
        docs = soup.find_all('doc')
        for doc in docs:
            id = doc.get('id')
            title = doc.get('title')
            #text = doc.get_text()



