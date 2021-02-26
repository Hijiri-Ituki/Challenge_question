
from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd

url = "https://kino-code.com/python-super-basic-course/"     #""の中にブログなどのURLを入力
response = req.urlopen(url)

parse_html = BeautifulSoup(response,'html.parser')

title_lists = parse_html.find_all('a')   #aタグについてはノート参照

title_list =[]

for i in title_lists:
    title_list.append(i.string)

url_list = []

for j in title_lists:
    if 'href' in j.attrs:
        url_list.append(j.attrs['href'])

dict_title_url = {'Title':title_list,'URL':url_list}
df_title_url = pd.DataFrame.from_dict(dict_title_url,orient='index').T

df_notnull = df_title_url.dropna(how='any')     #(how='any')は行に一つでも欠損値(None)があれば消去する記述

df_notnull['Title'].str.contains('Python超入門コース')

df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]   #[]の中にデータフレームにTrueとFalseのプール型を入れるとTrueだけが返ってくる

df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]

print(df_contain_python)
