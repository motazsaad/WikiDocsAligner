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


def usage():
    return '''args should be:
    source language,
    target language,
    source language links sql file,
    source corpus directory,
    target corpus directory,
    output directory'''


parser = argparse.ArgumentParser(description='Align Wikipedia documents based on interlanguage links .')

parser.add_argument('--srcLang', type=str, help='source language. '
                                                'For example, ar for Arabic, or'
                                                'en for English, or'
                                                'fr for French ...', required=True)
parser.add_argument('--targetLang', type=str, help='source language. '
                                                   'For example, ar for Arabic, or'
                                                   'en for English, or'
                                                   'fr for French ...', required=True)
parser.add_argument('--sqlFile', type=str, help='source language links sql file. '
                                                'Obtained from https://dumps.wikimedia.org/', required=True)
parser.add_argument('--srcCorpus', type=str, help='source corpus directory.', required=True)
parser.add_argument('--targetCorpus', type=str, help='target corpus directory.', required=True)
parser.add_argument('--outDir', type=str, help='the output directory.', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    src_lang = args.srcLang
    target_lang = args.targetLang
    src_ll_sql = args.sqlFile
    src_corpus_dir = args.srcCorpus
    target_corpus_dir = args.targetCorpus
    out_dir = args.outDir
    main(src_lang, target_lang, src_ll_sql, src_corpus_dir, target_corpus_dir, out_dir)

'''

python aligner.py ar arz /home/motaz/back09022017/wiki/arwiki-20170120-langlinks.sql /home/motaz/back09022017/wiki/arwiki /home/motaz/back09022017/wiki/arzwiki /home/motaz/tmp/out/

'''
