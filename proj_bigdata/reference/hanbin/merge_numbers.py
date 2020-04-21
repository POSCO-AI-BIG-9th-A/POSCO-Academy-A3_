import pandas as pd

df1 = pd.read_csv('numbers0~99.csv', engine='python')
df2 = pd.read_csv('numbers100~999.csv', engine='python')
df3 = pd.read_csv('numbers1000~1999.csv', engine='python')
df4 = pd.read_csv('numbers2000~2999.csv', engine='python')
df5 = pd.read_csv('numbers3000~3999.csv', engine='python')
df6 = pd.read_csv('numbers4000_4999.csv', engine='python')
df7 = pd.read_csv('numbers5000_.csv', engine='python')
df8 = pd.read_csv('numbers0~199.csv', engine='python')
df9 = pd.read_csv('numbers200~399.csv', engine='python')
df10 = pd.read_csv('numbers400~599.csv', engine='python')
df11 = pd.read_csv('numbers600~.csv', engine='python')



df_merge = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])

df_merge.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/numbers_raw.csv', header=True, index=False)
