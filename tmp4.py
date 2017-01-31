from bs4 import BeautifulSoup
import os
import parse_sql_script


def getTargetTitle(df, doc_id, ll_lang):
    return df.loc[(df.ll_from == doc_id) & (df.ll_lang == ll_lang), 'll_title'].values[0]


arz_df, ar_df = parse_sql_script.load_df()



print(getTargetTitle(ar_df, '7', 'arz'))