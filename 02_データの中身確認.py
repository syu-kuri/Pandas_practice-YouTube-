# 読み込んだデータdfの先頭3行、末尾10行を表示してください


import pandas as pd

df = pd.read_csv('weather.csv')
# ここまでは01_データの読み込みで終了済み


# -------------------
# 先頭3行の表示
df_head = df.head(3)
print(df_head)


# 末尾3行の表示
df_tail = df.tail(10)
print(df_tail)