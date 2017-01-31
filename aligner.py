import sys
import parse_sql_script
import os
import read_wiki_extracts


def main(src_lang, target_lang, src_ll_sql, target_ll_sql, src_corpus_dir, target_corpus_dir):
    print('source language:', src_lang)
    print('target language:', target_lang)
    src_df = parse_sql_script.sql2df(src_ll_sql)
    target_df = parse_sql_script.sql2df(target_ll_sql)
    src_corpus = read_wiki_extracts.load_corpus(src_corpus_dir)
    target_corpus = read_wiki_extracts.load_corpus(target_corpus_dir)



def usage():
    return "args should be: src_ll_sql, target_ll_sql, src_corpus_dir, target_corpus_dir"

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print(usage())
        sys.exit(0)
    else:
        src_lang = sys.argv[1]
        target_lang = sys.argv[2]
        src_ll_sql = sys.argv[3]
        target_ll_sql = sys.argv[4]
        src_corpus_dir = sys.argv[5]
        target_corpus_dir = sys.argv[6]
        main(src_ll_sql, target_ll_sql, src_corpus_dir, target_corpus_dir)