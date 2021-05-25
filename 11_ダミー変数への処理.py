# df_peopleのnationalityカラムをダミー変数に変換してください


import pandas as pd

df_people = pd.read_csv('people.csv')
# ここまでは08_重複除去で終了済み


# --------------
# pd.get_dummies()：ダミー変数への処理
df_dammies1 = pd.get_dummies(df_people['nationality'])
print(df_dammies1)

# 元のdf_peopleにダミー変数を結合
df_dammies2 = pd.get_dummies(df_people, columns=['nationality'])
print(df_dammies2)