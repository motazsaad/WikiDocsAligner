from ast import literal_eval as make_tuple
import ast
from io import StringIO
import re
import pandas as pd
import numpy as np
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
                        #print('\t'.join(record.replace('\'', '').split(',')))
                        sio.write('\t'.join(record.replace('\'', '').split(',')))
                        sio.write("\n")
                    except BaseException as error:
                        print('error: {0}'.format(error))
                        pass
    sio.seek(0)
    return sio


def load_df():
    arz_sql_file = "/home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql"  # mariadb records = 1015028
    ar_sql_file = "/home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql"  # mariadb records = 8693372

    arz_csv = read_sql_dump(dump_filename=arz_sql_file)
    arz_df = pd.read_csv(arz_csv, delimiter='\t', error_bad_lines=False)
    arz_selected = arz_df[arz_df.ll_lang == 'ar']

    ar_csv = read_sql_dump(dump_filename=ar_sql_file)
    ar_df = pd.read_csv(ar_csv, delimiter='\t', error_bad_lines=False)
    ar_selected = ar_df[ar_df.ll_lang == 'arz']

    return arz_selected, ar_selected

if __name__ == '__main__':
    arz_sql_file = "/home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql"  # mariadb records = 1015028
    ar_sql_file = "/home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql"  # mariadb records = 8693372

    arz_csv = read_sql_dump(dump_filename=arz_sql_file)
    arz_df = pd.read_csv(arz_csv, delimiter='\t', error_bad_lines=False)
    #print(arz_df)
    arz_selected = arz_df[arz_df.ll_lang == 'ar']

    ar_csv = read_sql_dump(dump_filename=ar_sql_file)
    ar_df = pd.read_csv(ar_csv, delimiter='\t', error_bad_lines=False)
    #print(ar_df)
    ar_selected = ar_df[ar_df.ll_lang == 'arz']
    print(ar_selected)



