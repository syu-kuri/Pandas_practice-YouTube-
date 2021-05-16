# 先頭行と、カラム名(列名)が「○○.1」「○○.2」となっているものを
# 削除したDataFrame dfを再定義してください


import pandas as pd

df = pd.read_csv('weather.csv')
# ここまでは01_データの読み込み、02_データの中身確認で終了済み


# ---------------
# Columnsを取得
df_columns = df.columns
# print(df_columns)

# 不要なものの削除
df = df[['年月日', 
'平均気温(℃)', 
'最高気温(℃)', 
'最高気温(℃).1', 
'降水量の合計(mm)', 
'最深積雪(cm)',
'平均雲量(10分比)', 
'平均蒸気圧(hPa)',
'平均風速(m/s)', 
'日照時間(時間)'
]][1:]                                    # [1:]は1行目から抽出したい場合

df_head = df.head(3)
df_tail = df.tail(10)

print(df_head)
print(df_tail)