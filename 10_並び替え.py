# dfを最高気温が高い順に並び変えてください

import pandas as pd

df = pd.read_csv('weather.csv')

df_columns = df.columns

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
]]

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


# --------------
# sort_values()：降順昇順の並び替えができる
df_down = df.sort_values('最高気温')            # 昇順の状態で表示される
print(df_down)

# sort_values(引数1, ascending=False)：降順になる
df_up = df.sort_values('最高気温', ascending=False)
print(df_up)