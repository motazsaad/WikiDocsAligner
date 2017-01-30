from ast import literal_eval as make_tuple
import ast
from io import StringIO
import re
import pandas as pd
import numpy as np

#sql_file = "/home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql" # mariadb records = 1015028
sql_file = "/home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql" # mariadb records = 8693372


def read_sql_dump(dump_filename):
    sio = StringIO()
    sio.write('''ll_from, ll_lang, ll_title\n''')
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
                        sio.write(record)
                        sio.write("\n")
                    except BaseException as error:
                        print('error: {0}'.format(error))
                        pass
    sio.seek(0)
    return sio


data = read_sql_dump(dump_filename=sql_file)
df = pd.read_csv(data, delimiter=',', error_bad_lines=False)
print(df)


