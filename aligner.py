import sys
import parse_sql_script
import os
import read_wiki_extracts
import worker


def main(src_lang, target_lang, src_ll_sql, src_corpus_dir, target_corpus_dir, out_dir):
    print('source language:', src_lang)
    print('target language:', target_lang)

    src_path = os.path.join(out_dir, src_lang)
    target_path = os.path.join(out_dir, target_lang)
    if not os.path.exists(src_path): os.makedirs(src_path)
    if not os.path.exists(target_path): os.makedirs(target_path)

    src_df = parse_sql_script.sql2df(src_ll_sql, target_lang)
    print(src_df)
    print("inter-language links sql file loaded successfully")

    src_corpus = worker.load_corpus(src_corpus_dir)
    target_corpus = worker.load_corpus(target_corpus_dir)
    print("source and target corpus loaded successfully")
    worker.doJob(src_lang, target_lang, src_df, src_corpus, target_corpus, out_dir)


def usage():
    return "args should be: src_lang, target_lang, src_ll_sql, src_corpus_dir, target_corpus_dir, out_dir"


if __name__ == '__main__':
    if len(sys.argv) < 7:
        print(usage())
        sys.exit(0)
    else:
        src_lang = sys.argv[1]
        target_lang = sys.argv[2]
        src_ll_sql = sys.argv[3]
        src_corpus_dir = sys.argv[4]
        target_corpus_dir = sys.argv[5]
        out_dir = sys.argv[6]
        main(src_lang, target_lang, src_ll_sql, src_corpus_dir, target_corpus_dir, out_dir)


'''
python3 aligner.py arz ar /home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql /home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql /home/motaz/Downloads/wiki/arzwiki /home/motaz/Downloads/wiki/arwiki /home/motaz/tmp/out/

python3 aligner.py ar arz /home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql /home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql /home/motaz/Downloads/wiki/arwiki /home/motaz/Downloads/wiki/arzwiki /home/motaz/tmp/out/

python3 aligner.py ar arz /home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql /home/motaz/Downloads/wiki/arwiki /home/motaz/Downloads/wiki/arzwiki /home/motaz/tmp/out/


'''