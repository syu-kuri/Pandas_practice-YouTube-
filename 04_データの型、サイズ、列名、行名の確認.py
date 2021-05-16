# 下記の値を取得しなさい
# ・各列のデータ型
# ・DataFrameのサイズ
# ・列名
# ・行名


import pandas as pd

df = pd.read_csv('weather.csv')

df = df[['年月日', 
'平均気温(℃)', 
'最高気温(℃)',
'最低気温(℃)',
'降水量の合計(mm)', 
'最深積雪(cm)',
'平均雲量(10分比)', 
'平均蒸気圧(hPa)',
'平均風速(m/s)', 
'日照時間(時間)'
]][1:]

df_head = df.head(3)
df_tail = df.tail(10)
# ここまでは01_データの読み込み～03_不要な列、行の削除で終了済み


# ---------------
# Colunmsのデータ型を確認
df_types = df.dtypes
print(df_types)

# サイズの確認
df_shape = df.shape
print(df_shape)

# カラムの表示
df_columns = df.columns

# 番号の取得
df_index = df.index
print(df_index)