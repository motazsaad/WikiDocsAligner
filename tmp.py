from ast import literal_eval as make_tuple
import ast
import re


print(make_tuple("(1,2,3,4,5)"))
mylist = ast.literal_eval('''(9140,'aa','Category:User de'),(25539,'aa','Category:User de-1'),(98724,'aa','Main Page')''')
for l in mylist:
    print(l)


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
            print(data)
            for d in data:
                try:
                    print(d)
                    #newline = d.strip(' ()')
                    #newline = newline.replace('`', '')
                    #print(newline.split(','))
                    #print(len(newline.strip().split(',')))
                    #row = newline.strip().split(',')
                    records.append([d[0], d[1], d[3]])
                except IndexError:
                    pass
            if line.endswith(';'):
                break
    #sio.seek(0)
    return records

# count = 0
# with open(sql_file, encoding='utf-8', errors='replace') as sql_reader:
#     lines = sql_reader.readlines()
#     print('line numbers', len(lines))
#     insert_lines = list()
#     for line in lines:
#         if line.startswith("INSERT"):
#             insert_lines.append(line)
#     print('insert line numbers', len(insert_lines))
#     #print(insert_lines[0])
#     values = insert_lines[0].replace('INSERT INTO `langlinks` VALUES ', '')
#     #print(values)
#     #values_list = ast.literal_eval(values)
#     # print(values_list[0])
#     # prin