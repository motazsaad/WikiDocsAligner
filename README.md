# WikiDocsAligner: Wikipedia Documents Aligner 
Align Wikipedia documents based on interlanguage links 


## Installation

To use this tool, you must install requirements 

```pip install -r requirements.txt```

## Usage example:

### aligner.py
align wikipedia documents given that you have the sql of interlanugage links and document extracts 

```python aligner.py ar arz data/arwiki-20170120-langlinks.sql data/wiki/arwiki data/wiki/arzwiki data/out/```



### corpus_info.py
to get information about the corpus (the most frequent words)

```python corpus_info.py data/arz.wiki```


## Related projects
This project is used to extract [Comparable Documents from Wikipedia](https://github.com/motazsaad/comparableWikiCoprus/)


#### To cite this tool:

Motaz Saad (2017). _WikiDocsAligner: an off-the-shelf Wikipedia Documents Alignment Tool_. in The Second Palestinian International Conference on Information and
Communication Technology (PICICT 2017). 
