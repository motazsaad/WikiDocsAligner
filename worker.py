import os

def getTargetTitle(df, doc_id, ll_lang):
    return df.loc[(df.ll_from == doc_id) & (df.ll_lang == ll_lang), 'll_title'].values[0]


def getDocByTitle(title, corpus):
    for wiki_doc in corpus:
        doc_id, doc_title, doc = wiki_doc
        if doc_title == title:
            return wiki_doc
    return None

def save_docs(aligned_docs, out_dir, src_lang, target_lang):
    src_path = os.path.join(out_dir, src_lang)
    target_path = os.path.join(out_dir, target_lang)
    if not os.path.exists(src_path): os.makedirs(src_path)
    if not os.path.exists(target_path): os.makedirs(target_path)
    for s,t in aligned_docs:



def doJob(src_lang, target_lang, src_df, target_df, src_corpus, target_corpus, out_dir):
    aligned_docs = list()
    for src_doc in src_corpus:
        doc_id, title, doc = src_doc
        target_title = getTargetTitle(src_df, doc_id, target_lang)
        target_doc = getDocByTitle(target_title, target_corpus)
        aligned_docs.append((src_doc, target_doc))

    save_docs(aligned_docs, out_dir, src_lang, target_lang)
