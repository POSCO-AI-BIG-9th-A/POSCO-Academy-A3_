import pandas as pd
import re

df = pd.read_csv('CountryRanking_raw.csv',engine='python')


com_dom_bo = []
for i in range(len(df['avrg_budget'])):
    p = re.findall(r'\d+', df['avrg_budget'][i])
    p = ''.join(p)
    com_dom_bo.append(int(p))
com_wrld_bo = []
for i in range(len(df['country_wrld_bo'])):
    p = re.findall(r'\d+', df['country_wrld_bo'][i])
    p = ''.join(p)
    com_wrld_bo.append(int(p))

data = []
data.append(df['prd_country']);data.append(df['num_movies']); data.append(com_dom_bo); data.append(com_wrld_bo)

columns = ['prd_country','num_movies','avrg_budget','country_wrld_bo']
newData = dict()
for (col, d) in zip(columns, data):
    newData[col] = d
df = pd.DataFrame(newData, columns=columns)
df.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/CountryRanking.csv', header=True, index=False)