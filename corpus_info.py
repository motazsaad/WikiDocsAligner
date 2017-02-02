import os
import sys
import worker


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))


def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def info(corpus_dir, topn=10):
    corpus = worker.load_corpus(corpus_dir)
    word_list = list()
    for i, t, d in corpus:
        word_list.extend(d.get_text().split())
    #print(word_list[:10])
    words = len(word_list)
    vocabulary = len(set(word_list))
    print("words: {0}\t vocabulary: {1}".format(words, vocabulary))
    dict = wordListToFreqDict(word_list)
    sorteddict = sortFreqDict(dict)
    for s in sorteddict[:topn]: print(str(s))




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage corpus_inf.py <corpus dir>")
    else:
        corpus_dir = sys.argv[1]
        info(corpus_dir)




