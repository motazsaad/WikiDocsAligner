import os
import sys
from bs4 import BeautifulSoup


def get_target_title(df, doc_id, ll_lang):
    try:
        title = df.loc[(df.ll_from == doc_id) & (df.ll_lang == ll_lang), 'll_title'].values[0]
        return title
    except IndexError as error:
        return None


def get_doc_by_title(title, corpus):
    for wiki_doc in corpus:
        doc_id, doc_title, doc = wiki_doc
        if doc_title == title:
            return wiki_doc
    return None


def write_file(f, doc):
    doc_id, title, d = doc
    with open(f, 'w') as file_writer:
        file_writer.write(str(d))
        file_writer.close()


def save_docs(src_doc, target_doc, src_lang, target_lang, out_dir, file_count):
    src_path = os.path.join(out_dir, src_lang)
    target_path = os.path.join(out_dir, target_lang)
    file_name = "doc_{:06d}.txt".format(file_count)
    src_out = os.path.join(src_path, file_name)
    target_out = os.path.join(target_path, file_name)
    write_file(src_out, src_doc)
    write_file(target_out, target_doc)


def do_work(src_lang, target_lang, src_df, src_corpus, target_corpus, out_dir):
    print("aligning documents ...")
    print("source corpus size: {0} documents".format(len(src_corpus)))
    aligned_count = 0
    processed_count = 0
    for src_doc in src_corpus:
        doc_id, title, doc = src_doc
        target_title = get_target_title(src_df, doc_id, target_lang)
        if target_title:
            target_doc = get_doc_by_title(target_title, target_corpus)
            if target_doc:
                save_docs(src_doc, target_doc, src_lang, target_lang, out_dir, aligned_count)
                aligned_count += 1
        sys.stdout.write("\rdocuments processed: {0}\t\tdocuments aligned: {1}".format(processed_count, aligned_count))
        sys.stdout.flush()
        processed_count += 1
    print("\nwriting aligned documents completed successfully!")


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
