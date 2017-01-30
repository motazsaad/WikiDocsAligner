from ast import literal_eval as make_tuple
import ast
from io import StringIO
import re
import pandas as pd

sql_file = "/home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql"
#sql_file = "/home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql"


def read_dump(dump_filename, target_table):
    #sio = StringIO()
    records = list()
    fast_forward = True
    with open(dump_filename, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith('insert') and target_table in line:
                fast_forward = False
            if fast_forward:
                continue
            data = re.findall('\([^\)]*\)', line)
            #print(data)
            for d in data:
                try:
                    newline = d.strip(' ()')
                    newline = newline.replace('`', '')
                    #print(newline.split(','))
                    #print(len(newline.strip().split(',')))
                    records.append(newline.strip().split(','))
                except IndexError:
                    pass
            if line.endswith(';'):
                break
    #sio.seek(0)
    return records




data = read_dump(dump_filename=sql_file, target_table='langlinks')
#print(arz_langlinks_csv.readlines())
df_arz_langlinks = pd.DataFrame(data)
print(df_arz_langlinks)




count = 0
with open(sql_file, encoding='utf-8', errors='replace') as sql_reader:
    lines = sql_reader.readlines()
    print('line numbers', len(lines))
    insert_lines = list()
    for line in lines:
        if line.startswith("INSERT"):
            insert_lines.append(line)
    print('insert line numbers', len(insert_lines))
    #print(insert_lines[0])
    values = insert_lines[0].replace('INSERT INTO `langlinks` VALUES ', '')
    #print(values)
    #values_list = ast.literal_eval(values)
    # print(values_list[0])
    # print(values_list[1])