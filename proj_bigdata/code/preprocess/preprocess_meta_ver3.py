import pandas as pd
import numpy as np

# studio_score/price_class/contract_price 계산
df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned_ver4.csv", engine= "python", encoding='utf-8')
df_meta = df_meta.drop('Unnamed: 0', axis = 1)

df_meta = df_meta.drop(["studio_score","price_class", "contract_price"], axis = 1)

df_meta["studio_score"] = '.'
df_meta["price_class"] = '.'
df_meta["contract_price"] = '.'

df_meta["cnt_movie"] = 0
# studio_score
prd_cnt = df_meta[df_meta['studio'] != '.']
prd_cnt = prd_cnt.groupby(['studio']).count()
prd_cnt = prd_cnt['cnt_movie']

cnt_base_50 = int(prd_cnt.quantile(.915))
cnt_base_20 = int(prd_cnt.quantile(.83))
cnt_base_10 = int(prd_cnt.quantile(.73))

budget_mid = df_meta[['studio', 'budget']]
budget_mid = budget_mid[budget_mid['budget']!= '.']
budget_mid.reset_index()

budget_mid["budget"] = budget_mid["budget"].astype(float)

budget_mid = budget_mid.groupby(['studio']).median()
budget_mid = budget_mid['budget']

budget_base_50000000 = int(budget_mid.quantile(.95))
budget_base_20000000 = int(budget_mid.quantile(.60))
budget_base_5000000 = int(budget_mid.quantile(.15))

prd_list = pd.merge(prd_cnt, budget_mid, on ='studio')
prd_list["studio_score"] = 0

for i in prd_list.index:
    if prd_list['cnt_movie'][i] >= cnt_base_50 and prd_list['budget'][i] >= budget_base_50000000 :
         prd_list.loc[i,'studio_score'] = int(10)
    elif prd_list['cnt_movie'][i]  >= cnt_base_20 and prd_list['budget'][i] >= budget_base_20000000 :
         prd_list.loc[i,'studio_score'] = int(6)
    elif prd_list['cnt_movie'][i]  >= cnt_base_10 or prd_list['budget'][i] >= budget_base_20000000 :
         prd_list.loc[i,'studio_score'] = int(4)
    elif prd_list['cnt_movie'][i] >= cnt_base_10 or prd_list['budget'][i] >= budget_base_5000000:
         prd_list.loc[i,'studio_score'] = int(2)
    else :
        prd_list.loc[i, 'studio_score'] = int(1)

for i in range(len(df_meta)):
    for j in prd_list.index:
        if df_meta['studio'][i] == j:
            df_meta.loc[i, "studio_score"] = int(prd_list.loc[j,'studio_score'])

# price_class
for col in df_meta.columns:
    df_meta.loc[df_meta[col].isna(), col] = '.'

df_price = df_meta[df_meta["income_usa"] != "."]
df_price = df_price.reset_index()

df_price["income_usa"] = df_price["income_usa"].astype(float)

avg_income_usa = np.mean(df_price["income_usa"])
med_income_usa = np.median(df_price['income_usa'])

df_price = df_price[df_price["imdb_score"] != "."]
df_price = df_price.reset_index()
df_price["imdb_score"] = df_price["imdb_score"].astype(float)

avg_imdb_score = np.mean(df_price['imdb_score'])
std_imdb_score = np.std(df_price['imdb_score'])

print("avg_income_usa : %0.2f"%(avg_income_usa))
print("med_income_usa : %0.2f" %(med_income_usa))
print("avg_imdb_score : %0.2f" %(avg_imdb_score))
print("std_imdb_score : %0.2f"%(std_imdb_score))

for i in range(len(df_price)):
    mId = df_price["movie_id"][i]
    if df_price['income_usa'][i] > avg_income_usa and df_price['imdb_score'][i] > (avg_imdb_score + std_imdb_score):
        df_meta.loc[(df_meta["movie_id"]== mId),'price_class'] = int(10)
    elif df_price['income_usa'][i] > med_income_usa and df_price['imdb_score'][i] > (avg_imdb_score + std_imdb_score):
        df_meta.loc[(df_meta["movie_id"]== mId),'price_class'] = int(5)
    elif med_income_usa <= df_price['income_usa'][i] <= avg_income_usa :
        df_meta.loc[(df_meta["movie_id"]== mId),'price_class'] = int(3)
    else:
        df_meta.loc[(df_meta["movie_id"]== mId),'price_class'] = int(1)

cnt = 0
for i in range(len(df_meta)):
    if df_meta["studio_score"][i] != "." and df_meta["price_class"][i] != ".":
        studio_score = int(float(df_meta["studio_score"][i]))
        price_class = int(float(df_meta["price_class"][i]))
        df_meta['contract_price'][i] = int(500) + int(studio_score) * 20 + int(price_class) * 30
        cnt += 1

print(cnt)
df_meta = df_meta.drop('cnt_movie', axis = 1)

df_meta.to_csv('../../data/cleaned/movie_meta_cleaned_ver5.csv', header=True, index=False)