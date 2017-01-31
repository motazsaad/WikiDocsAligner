from bs4 import BeautifulSoup
import os
import parse_sql_script



'''
arz:
SELECT * FROM ar_langlinks
where ar_langlinks.ll_lang = 'arz' and ar_langlinks.ll_title = 'ميه'
;

'7', 'arz', 'ميه'


ar:
SELECT * FROM arz_langlinks
where arz_langlinks.ll_lang = 'ar' and arz_langlinks.ll_title = 'ماء'
;
'35097', 'ar', 'ماء'





'''




