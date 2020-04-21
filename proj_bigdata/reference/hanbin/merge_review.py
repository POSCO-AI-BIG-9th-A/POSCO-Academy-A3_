import pandas as pd

df1 = pd.read_csv('NumOfReviews1000.csv', engine='python')
df2 = pd.read_csv('NumOfReviews2000.csv', engine='python')
df3 = pd.read_csv('NumOfReviews3000.csv', engine='python')
df4 = pd.read_csv('NumOfReviews4000.csv', engine='python')
df5 = pd.read_csv('NumOfReviews5000.csv', engine='python')
df6 = pd.read_csv('NumOfReviews6000.csv', engine='python')


df_merge = pd.concat([df1,df2,df3,df4,df5,df6])

df_merge.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/NumOfReviews.csv', header=True, index=False)
