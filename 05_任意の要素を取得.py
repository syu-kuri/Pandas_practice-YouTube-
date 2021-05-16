# dfの5~10行目、3~6列目(最高気温(℃)~最深積雪(cm))の要素を取得してください


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

df_types = df.dtypes
df_shape = df.shape
df_columns = df.columns
df_index = df.index
# ここまでは01_データの読み込み～04_データの型、サイズ、列名、行名の確認で終了済み


# ---------------
# iloc[行, 列] or loc[行, 列]で任意の要素を取得

# 任意の要素を取得(iloc編)
df_iloc = df.iloc[4:10, 2:6]                                    # ilocは要素番号(インデックス)で指定
print(df_iloc)

# 任意の要素を取得(loc編)
df_loc = df.loc[5:10, '最高気温(℃)':'最深積雪(cm)']            # locはカラム名で指定
print(df_loc)