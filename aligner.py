import argparse
import sys
import parse_sql_script
import os
import worker


def main(src_lang, target_lang, src_ll_sql, src_corpus_dir, target_corpus_dir, out_dir):
    print('source language:', src_lang)
    print('target language:', target_lang)
    print('source language links sql file', src_ll_sql)
    print('source corpus directory', src_corpus_dir)
    print('target corpus directory', target_corpus_dir)
    print('output directory', out_dir)

    src_path = os.path.join(out_dir, src_lang)
    target_path = os.path.join(out_dir, target_lang)
    if not os.path.exists(src_path): os.makedirs(src_path)
    if not os.path.exists(target_path): os.makedirs(target_path)

    src_df = parse_sql_script.sql2df(src_ll_sql, target_lang)

    print("inter-language links sql file loaded successfully")

    src_corpus = worker.load_corpus(src_corpus_dir)
    target_corpus = worker.load_corpus(target_corpus_dir)
    print("source and target corpus loaded successfully")
    worker.do_work(src_lang, target_lang, src_df, src_corpus, target_corpus, out_dir)





parser = argparse.ArgumentParser(description='Align Wikipedia documents based on interlanguage links .')

parser.add_argument('--src-lang', type=str, help='source language. '
                                                'e.g., ar for Arabic, '
                                                'en for English, or '
                                                'fr for French ...', required=True)
parser.add_argument('--target-lang', type=str, help='target language. '
                                                   'e.g., ar for Arabic, '
                                                   'en for English, or '
                                                   'fr for French ...', required=True)
parser.add_argument('--sql-file', type=str, help='source language links sql file. '
                                                'Obtained from https://dumps.wikimedia.org/', required=True)
parser.add_argument('--src-corpus', type=str, help='source corpus directory.', required=True)
parser.add_argument('--target-corpus', type=str, help='target corpus directory.', required=True)
parser.add_argument('--out-dir', type=str, help='the output directory.', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    src_lang = args.src_lang
    target_lang = args.target_lang
    src_ll_sql = args.sql_file
    src_corpus_dir = args.src_corpus
    target_corpus_dir = args.target_corpus
    out_dir = args.out_dir
    main(src_lang, target_lang, src_ll_sql, src_corpus_dir, target_corpus_dir, out_dir)

'''

python aligner.py ar arz /home/motaz/back09022017/wiki/arwiki-20170120-langlinks.sql /home/motaz/back09022017/wiki/arwiki /home/motaz/back09022017/wiki/arzwiki /home/motaz/tmp/out/

'''
