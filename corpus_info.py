import os
import sys
import worker
import operator
from tabulate import tabulate
from bs4 import BeautifulSoup



def remove_punctuations(text):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~،'
    return ''.join(ch for ch in text if ch not in punctuations)

def info(corpus_file, topn=30):
    print("reading corpus ...")
    corpus = open(corpus_file).read()
    print("striping html tags")
    soup = BeautifulSoup(corpus, 'html.parser')
    del corpus
    print("removing punctuations")
    clean_corpus = remove_punctuations(soup.get_text())
    del soup
    print("get the words list")
    words = clean_corpus.split()
    del clean_corpus
    print("start to count frequencies")
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sortedFreq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

    top = [list(i) for i in sortedFreq[:topn]]  # list of lists
    return top




if __name__ == '__main__':
    #arz = "/home/motaz/tmp/out/arz.wiki"
    #ar = "/home/motaz/tmp/out/ar.wiki"

    #arz_top = info(arz)
    #ar_top = info(ar)

    # for l1,l2 in zip(arz_top, ar_top):
    #     print("\RL{" + l1[0] + "}\t\t&\t\t" + str(l1[1]) + "\t&\t\RL{" + l2[0] + "}\t\t&\t\t" + str(l2[1]) + "\t\\\\")

    arz = "/home/motaz/Downloads/wiki/arz.wiki"
    ar = "/home/motaz/Downloads/wiki/ar.wiki"


    # arz_top = info(arz)
    # for l in arz_top:
    #     print("\RL{" + l[0] + "}\t\t&\t\t" + str(l[1]) + "\t\\\\")

    ar_top = info(ar)
    for l in ar_top:
        print("\RL{" + l[0] + "}\t\t&\t\t" + str(l[1]) + "\t\\\\")



#table = [a+b for a,b in zip(arz_top,ar_top)]

    #print(tabulate(top, headers=["Egyptian Word", "Frequency"], tablefmt="latex"))
    #print(tabulate(table, headers=["Egyptian Word", "Frequency", "Arabic Word", "Frequency"], tablefmt="latex"))

    # if len(sys.argv) < 2:
    #     print("usage corpus_inf.py <corpus dir>")
    # else:
    #     corpus_dir = sys.argv[1]
    #     info(corpus_dir)




