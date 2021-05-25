# dfの欠損値を列方向で削除してください


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

df.columns = ['年月日', 
              '平均気温', 
              '最高気温',
              '最低気温',
              '降水量の合計', 
              '最深積雪',
              '平均雲量', 
              '平均蒸気圧',
              '平均風速', 
              '日照時間']
# ここまでは09_カラム名変更で終了済み

# -----------
# isnull().sum()で欠損値の数を確認
df_isnull_sum = df.isnull().sum()
print(df_isnull_sum)

# dropna()：欠損値の削除
# axis = 1：列方向、axis = 0：行方向
df_dropna = df.dropna(axis=1)
print(df_dropna)