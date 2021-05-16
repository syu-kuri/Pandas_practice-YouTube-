# people.csvを読み込みdf_peopleと定義してください
# その後、下記の条件を満たすDataFrameをそれぞれ抽出してください
# ・nationality が America である
# ・age が 20以上30未満である


import pandas as pd

df_people = pd.read_csv('people.csv')
# ここまでは01_データの読み込みで終了済み



# --------------------
# 条件抽出にはメソッドを使用しないやり方とquery()を使用したやり方がある


# nationality が America であるものの抽出
# メソッドを使用しないやり方
nationality_America1 = df_people[df_people['nationality'] == 'America']
print(nationality_America1)

# query()を使用したやり方
nationality_America2 = df_people.query('nationality == "America"')
print(nationality_America2)

# isinを使用したやり方 
nationality_America3 = df_people[df_people['nationality'].isin(['America'])]
print(nationality_America3)


# age が 20以上30未満であるものの抽出
# メソッドを使用しないやり方
age1 = df_people[(df_people['age'] >= 20) & (df_people['age'] < 30)]
print(age1)

# query()を使用したやり方
age2 = df_people.query('age >= 20 & age < 30')
print(age2)