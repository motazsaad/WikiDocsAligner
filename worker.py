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


def save_docs(src_doc, target_doc, out_dir, file_count):
    file_name = "doc_{:06d}.txt".format(file_count)
    src_out = os.path.join(out_dir, file_name)
    target_out = os.path.join(out_dir, file_name)
    write_file(src_out, src_doc)
    write_file(target_out, target_doc)



def doJob(src_lang, target_lang, src_df, src_corpus, target_corpus, out_dir):
    print("aligning documents ...")
    print("source corpus size: {0} documents".format(len(src_corpus)))
    aligned_count = 0
    processed_count = 0
    for src_doc in src_corpus:
        doc_id, title, doc = src_doc
        target_title = getTargetTitle(src_df, doc_id, target_lang)
        if target_title:
            target_doc = getDocByTitle(target_title, target_corpus)
            save_docs(src_doc, target_doc, out_dir, aligned_count)
            aligned_count += 1
        sys.stdout.write("\rdocuments processed: {0}\t\tdocuments aligned: {1}".format(processed_count, aligned_count))
        sys.stdout.flush()
        processed_count += 1
    print("writing aligned documents completed successfully!")
