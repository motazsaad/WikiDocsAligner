# WikiDocsAligner: Wikipedia Documents Aligner 
Align Wikipedia documents based on interlanguage links 


## Installation

To use this tool, you must install requirements 

```pip install -r requirements.txt```

## Usage example:

### aligner.py
align wikipedia documents given that you have the sql of interlanugage links and document extracts 

```python aligner.py --srcLang ar --targetLang arz --sqlFile data/arwiki-20170120-langlinks.sql --srcCorpus data/wiki/arwiki --targetCorpus data/wiki/arzwiki --outDir data/out/```

### Arguments
```
usage: aligner.py [-h] --srcLang SRCLANG --targetLang TARGETLANG --sqlFile
                  SQLFILE --srcCorpus SRCCORPUS --targetCorpus TARGETCORPUS
                  --outDir OUTDIR

Align Wikipedia documents based on interlanguage links .

optional arguments:
  -h, --help            show this help message and exit
  --srcLang SRCLANG     source language. e.g., ar for Arabic, en for English,
                        or fr for French ...
  --targetLang TARGETLANG
                        target language. e.g., ar for Arabic, en for English,
                        or fr for French ...
  --sqlFile SQLFILE     source language links sql file. Obtained from
                        https://dumps.wikimedia.org/
  --srcCorpus SRCCORPUS
                        source corpus directory.
  --targetCorpus TARGETCORPUS
                        target corpus directory.
  --outDir OUTDIR       the output directory.


```

### corpus_info.py
to get information about the corpus (the most frequent words)

```python corpus_info.py data/arz.wiki```


## Related projects
This project is used to extract [Comparable Documents from Wikipedia](https://github.com/motazsaad/comparableWikiCoprus/)


#### To cite this tool:

Motaz Saad and Basem Alijla (2017). _WikiDocsAligner: an off-the-shelf Wikipedia Documents Alignment Tool_. in The Second Palestinian International Conference on Information and Communication Technology (PICICT 2017). 


## How to contribute
Your contributions to improve the code are welcomed. Please follow the steps below.
1. Fork the project.
2. Modify the code, test it, make sure that it works fine. 
3. Make a pull request.

Please consult [github help](https://help.github.com/) to get help.
