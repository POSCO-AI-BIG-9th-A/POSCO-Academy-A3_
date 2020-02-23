import pandas as pd
import re

df = pd.read_csv('ProductionRanking_raw.csv',engine='python')


com_dom_bo = []
for i in range(len(df['com_dom_bo'])):
    p = re.findall(r'\d+', df['com_dom_bo'][i])
    p = ''.join(p)
    com_dom_bo.append(int(p))
com_wrld_bo = []
for i in range(len(df['com_wrld_bo'])):
    p = re.findall(r'\d+', df['com_wrld_bo'][i])
    p = ''.join(p)
    com_wrld_bo.append(int(p))

data = []
data.append(df['prd_company']);data.append(df['num_movies']); data.append(com_dom_bo); data.append(com_wrld_bo)

columns = ['prd_company','num_movies','com_dom_bo','com_wrld_bo']
newData = dict()
for (col, d) in zip(columns, data):
    newData[col] = d
df = pd.DataFrame(newData, columns=columns)
df.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/ProductionRanking.csv', header=True, index=False)