from bs4 import BeautifulSoup
import os
import parse_sql_script


def ge_title(df, doc_id, ll_lang):
    return df.loc[df['ll_from'] == doc_id, 'll_lang'].values[0]



arz_df, ar_df = parse_sql_script.load_df()



print(ge_title(ar_df, 7, 'arz'))