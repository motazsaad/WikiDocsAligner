import os
import sys


def getTargetTitle(df, doc_id, ll_lang):
    try:
        title = df.loc[(df.ll_from == doc_id) & (df.ll_lang == ll_lang), 'll_title'].values[0]
        return title
    except IndexError as error:
        return None


def getDocByTitle(title, corpus):
    for wiki_doc in corpus:
        doc_id, doc_title, doc = wiki_doc
        if doc_title == title:
            return wiki_doc
    return None


def write_file(f, doc):
    with open(f, 'w') as file_writer:
        file_writer.write(doc)
        file_writer.close()


def save_docs(aligned_docs, out_dir, src_lang, target_lang):
    src_path = os.path.join(out_dir, src_lang)
    target_path = os.path.join(out_dir, target_lang)
    if not os.path.exists(src_path): os.makedirs(src_path)
    if not os.path.exists(target_path): os.makedirs(target_path)
    file_count = 0
    for s, t in aligned_docs:
        file_name = "doc_{:06d}.txt".format(file_count)
        src_out = os.path.join(out_dir, file_name)
        target_out = os.path.join(out_dir, file_name)
        write_file(src_out, s)
        write_file(target_out, t)
        sys.stdout.write("\rdocuments aligned: {0}".format(file_count))
        sys.stdout.flush()
        file_count += 1
    print("\ndone!")




def doJob(src_lang, target_lang, src_df, target_df, src_corpus, target_corpus, out_dir):

    aligned_docs = list()
    for src_doc in src_corpus:
        doc_id, title, doc = src_doc
        target_title = getTargetTitle(src_df, doc_id, target_lang)
        if target_title:
            target_doc = getDocByTitle(target_title, target_corpus)
            aligned_docs.append((src_doc, target_doc))

    save_docs(aligned_docs, out_dir, src_lang, target_lang)
    print("writing aligned documents completed successfully!")
