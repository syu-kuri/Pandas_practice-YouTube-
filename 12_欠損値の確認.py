# dfの欠損値を確認してください

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


# -------------
# isnull：欠損値 = True 値が入っている = False
df_isnull = df.isnull()
print(df_isnull)
