import os
import sys
import worker
import operator
from tabulate import tabulate
from bs4 import BeautifulSoup
import string


def remove_punctuations(text):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~،'
    return ''.join(ch for ch in text if ch not in punctuations)


def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation + "،")
    return s.translate(translator)


def info(corpus_file, topn=30):
    print("reading corpus ...")
    corpus = open(corpus_file).read()
    print("striping html tags")
    soup = BeautifulSoup(corpus, 'html.parser')
    clean_corpus = soup.get_text()
    del corpus
    del soup
    print("removing punctuations")
    clean_text = remove_punctuation(clean_corpus)
    del clean_corpus
    print("get the words list")
    words = clean_text.split()
    del clean_text
    stopwords = open("stopwords_arabic.ar").read().split()
    print("removing stopwords")
    words = [w for w in words if w not in stopwords]
    print("start to count frequencies")
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

    top = [list(i) for i in sorted_freq[:topn]]  # list of lists
    return top


def print_info_arabic(corpus):
    top = info(corpus)
    for item in top:
        print("\RL{" + item[0] + "}\t\t&\t\t" + str(item[1]) + "\t\\\\") # for latex if the text is arabic


def print_info(corpus):
    top = info(corpus)
    top_list = []
    print(tabulate(top, headers=["Word", "Frequency"], tablefmt="pipe"))


def usage():
    return "please provide a corpus file"


if __name__ == '__main__':
    if len(sys.argv) == 2:
        corpus = "/home/motaz/back09022017/wiki/arz.wiki"
        print_info(corpus)
    else:
        print(usage())
        sys.exit(-1)


#python corpus_info.py /home/motaz/back09022017/wiki/arz.wiki
