# dfd_people のnationalityの列に対し、重複のある値の行を除去した
# DataFrameを取得してください


import pandas as pd

df_people = pd.read_csv('people.csv')
# ここまでは07_ユニークな値の抽出で終了済み


# ---------------
# drop_duplicates()：重複を除去するメソッド
drop_duplicates = df_people.drop_duplicates(subset='nationality')
print(drop_duplicates)