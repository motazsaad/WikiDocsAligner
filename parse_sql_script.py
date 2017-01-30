sql_file = "/home/motaz/Downloads/wiki/arzwiki-20170120-langlinks.sql"
#sql_file = "/home/motaz/Downloads/wiki/arwiki-20170120-langlinks.sql"


count = 0
with open(sql_file, encoding='utf-8', errors='replace') as sql_reader:
    lines = sql_reader.readlines()
    print('line numbers', len(lines))
    insert_lines = list()
    for line in lines:
        if line.startswith("INSERT"):
            insert_lines.append(line)
    print('insert line numbers', len(insert_lines))
    print(insert_lines[0])