from ast import literal_eval as make_tuple
import ast
from io import StringIO
import re
import pandas as pd
import csv

#''''ll_from', 'll_lang', 'll_title'\n'''
#'''ll_from, ll_lang, ll_title\n'''

def read_sql_dump(dump_filename):
    sio = StringIO()
    sio.write('''ll_from\tll_lang\tll_title\n''')
    with open(dump_filename, 'r', encoding='utf-8', errors='replace') as f:

        for line in f:
            if line.startswith('INSERT INTO `langlinks` VALUES '):
                line = line.strip()
                line = line.replace('INSERT INTO `langlinks` VALUES ', '')
                line = line.replace('),', '\n')
                line = line.replace(");", "\n")
                data = line.split('\n')
                for d in data:
                    try:
                        record = d[1:]
                        sio.write('\t'.join(record.replace('\'', '').split(',')))
                        sio.write("\n")
                    except BaseException as error:
                        print('error: {0}'.format(error))
                        pass
    sio.seek(0)
    return sio


def sql2df(dump_filename, target_lang):
    my_csv = read_sql_dump(dump_filename)
    df = pd.read_csv(my_csv, delimiter='\t', error_bad_lines=False, warn_bad_lines=False)
    selected_df = df[df.ll_lang == target_lang]
    return selected_df





