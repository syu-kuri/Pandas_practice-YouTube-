# df_peopleに対して、カラム毎のユニーク(固有)な値を抽出してください


import pandas as pd

df_people = pd.read_csv('people.csv')
# ここまでは01_データの読み込みで終了済み


# ---------------
# unique()でユニークな値を抽出
# df_people.unique()ではエラーが起こる：uniqueは一次元にしか適用できない
# カラムを1つずつ指定してunique()を定義する

df_nationality_unique = df_people['nationality'].unique()
print(df_nationality_unique)

df_name_unique = df_people['name'].unique()
print(df_name_unique)

df_age_unique = df_people['age'].unique()
print(df_age_unique)