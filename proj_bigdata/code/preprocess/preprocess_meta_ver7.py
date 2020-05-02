import pandas as pd
import numpy as np
import math
from collections import Counter


df = pd.read_csv("../../data/cleaned/movie_meta_cleaned_ver6_transformed.csv", engine= "python", encoding='cp949')

df = df.drop('Unnamed: 0', axis = 1)

# String to num
col_numeric = ['release_year', 'release_date', 'runtime', 'imdb_score', 'dvd_sales', 'blu_sales', 'total_sales',
               'legs', 'share', 'inf_income_usa', 'theater_opening', 'theater_total',
               'metascore', 'big_awards_num', 'awards_win_num', 'awards_nomin_num',
               'reviews_users', 'reviews_critics', 'budget', 'series_new', 'income_opening',
               'votes', 'income_usa', 'income_int', 'income_ww', 'contract_price', 'studio_score', 'price_class','contract_year',
               'dvd_over_income', 'movie_down_sales', 'contract_price_inf', 'net_profit', 'studio_score', 'contract_price', 'inf']
for col in col_numeric:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# '.' to Nan
for col in df.columns:
        df.loc[df[col] == '.', col] = np.nan

# making film 제거
making = 0
for i in df.index:
    if 'making' in df['title'][i].lower():
        df.drop(i, inplace=True)
        making += 1
print('title에 "making"포함되는 영화 수', making)
unmasked = 0
for i in df.index:
    if 'unmasked' in df['title'][i].lower():
        df.drop(i, inplace=True)
        unmasked += 1
print('title에 "unmasked"포함되는 영화 수',unmasked)

# 2019년, 2020년 개봉 영화 제거
df = df[(df['release_year'] != 2019) & (df['release_year'] != 2020)]

# release_date 결측치 포함한 행 제거
df = df[df['release_date'].isna() == False]

# mpa_rating 결측치 포함한 행 제거
df = df[df['mpa_rating'].isna() == False]

# imdb_score 결측치 포함한 행 제거
df = df[df['imdb_score'].isna() == False]

# inf_income_usa 결측치 대체(가장 가까운 날짜의 inf을 이용하여 대체, income_usa가 결측인 경우 구할 수 없음)
df = df.reset_index()
a = 0
for i in df.index:
    temp = {}
    if (math.isnan(df['inf_income_usa'][i]) == True) & (math.isnan(df['income_usa'][i]) == False):
        for j in df[df['inf'].isna() == False].index:
            if i != j:
                temp.update({abs(df['release_date'][i] - df['release_date'][j]): j})

        df['inf_income_usa'][i] = df['income_usa'][i] * df['inf'][temp.get(min(temp.keys()))]
        print(df['inf_income_usa'][i], i, df['income_usa'][i], df['inf'][temp.get(min(temp.keys()))],
              temp.get(min(temp.keys())))
        a += 1
print(a)

# inf_income_usa 이용하여 inf 결측치 대체
def inflation():
    global df
    df['inf'] = np.nan
    for i in df.index:
            if (math.isnan(df.loc[i, 'inf_income_usa']) == False) & (math.isnan(df.loc[i, 'income_usa']) == False) & (
                    df.loc[i, 'income_usa'] != 0):
                    df.loc[i, 'inf'] = float(df.loc[i, 'inf_income_usa']) / float(df.loc[i, 'income_usa'])
            else:
                    pass
inflation()

# src 결측치 최빈값으로 대체
nan_idx = np.argwhere([df['src'].isna()])
for i in nan_idx:
    df.loc[i[1],'src'] = 'original screenplay'

# reviews_users, reviews_critics 결측치 0으로 대체
for i in df.index:
    if math.isnan(df['reviews_users'][i]):
        df.loc[i,'reviews_users'] = 0
    if math.isnan(df['reviews_critics'][i]):
        df.loc[i,'reviews_critics'] = 0

# prd_mthd 결측치 최빈값으로 대체
nan_idx = np.argwhere([df['prd_mthd'].isna()])
for i in nan_idx:
    df['prd_mthd'][i[1]] = 'live action'

# studio 결측치 포함한 행 제거
df = df[df['studio'].isna() == False]

# director 결측치 포함한 행 제거
df = df[df['director'].isna() == False]

# 영어/비영어 파생변수 생성
df['english'] = 0
for i in df.index:
    if 'english' in df['language'][i].lower():
        df.loc[i,'english']= 1

# dvd, bluray 발매여부 파생변수 생성
df['dvd'] = 0
for i in df.index:
    if math.isnan(df['dvd_sales'][i]) == False:
        df.loc[i,'dvd'] = 1
df['blu'] = 0
for i in df.index:
    if math.isnan(df['blu_sales'][i]) == False:
        df.loc[i,'blu'] = 1

# 미국 제작 파생변수 생성
df['cntry_USA'] = 0
for i in df.index:
    if 'USA' in df['country'][i]:
        df.loc[i,'cntry_USA'] = 1

# actor_A, actor_B, actor_C 파생변수 생성
actor_list = []
for actor in df['actor_1']:
    actor_list.append(actor)
for actor in df['actor_2']:
    actor_list.append(actor)
for actor in df['actor_3']:
    actor_list.append(actor)
for actor in df['actor_4']:
    actor_list.append(actor)
actor_dic = Counter(actor_list)
actor_A = { key: value for key, value in actor_dic.items() if value > 9 }
actor_B = { key: value for key, value in actor_dic.items() if (value < 10) & (value > 4) }
actor_C = { key: value for key, value in actor_dic.items() if (value < 5) & (value > 1)}
print('A급, B급, C급, : {}, {}, {}'.format(len(actor_A),len(actor_B),len(actor_C)))
df['actor_A'] = 0 # actor_A는 10작품 이상 주연: A급, 238명 (전체 9202명)
for i in df.index:
    if df.loc[i,'actor_1'] in actor_A.keys():
        df.loc[i,'actor_A'] += 1
    if df.loc[i,'actor_2'] in actor_A.keys():
        df.loc[i,'actor_A'] += 1
    if df.loc[i,'actor_3'] in actor_A.keys():
        df.loc[i,'actor_A'] += 1
    if df.loc[i,'actor_4'] in actor_A.keys():
        df.loc[i,'actor_A'] += 1
df['actor_B'] = 0 # actor_B는 5작품 이상 10작품 미만 주연: B급, 639명
for i in df.index:
    if df.loc[i,'actor_1'] in actor_B.keys():
        df.loc[i,'actor_B'] += 1
    if df.loc[i,'actor_2'] in actor_B.keys():
        df.loc[i,'actor_B'] += 1
    if df.loc[i,'actor_3'] in actor_B.keys():
        df.loc[i,'actor_B'] += 1
    if df.loc[i,'actor_4'] in actor_B.keys():
        df.loc[i,'actor_B'] += 1
df['actor_C'] = 0# actor_C는 2작품 이상 5작품 미만 주연: C급, 1995명
for i in df.index:
    if df.loc[i,'actor_1'] in actor_C.keys():
        df.loc[i,'actor_C'] += 1
    if df.loc[i,'actor_2'] in actor_C.keys():
        df.loc[i,'actor_C'] += 1
    if df.loc[i,'actor_3'] in actor_C.keys():
        df.loc[i,'actor_C'] += 1
    if df.loc[i,'actor_4'] in actor_C.keys():
        df.loc[i,'actor_C'] += 1

# director_A, director_B, director_C 파생변수 생성
director_list = []
for director in df['director']:
    if ',' in director:
        d_list = director.split(',')
        for d in d_list:
            director_list.append(d.strip())
    else:
        director_list.append(director)
director_dic = Counter(director_list)
director_A = { key: value for key, value in director_dic.items() if value > 11 }
director_B = { key: value for key, value in director_dic.items() if (value < 12) & (value > 6) }
director_C = { key: value for key, value in director_dic.items() if (value < 7) & (value > 2) }
print('A급, B급, C급, : {}, {}, {}'.format(len(director_A),len(director_B),len(director_C)))
df['director_A'] = 0 # director_A는 12작품 이상 연출: A급, 27명 (총 2358명)
for i in df.index:
    if df.loc[i,'director'] in director_A.keys():
        df.loc[i,'director_A'] += 1
df['director_B'] = 0 # director_B는 7작품 이상 12작품 미만 연출: B급, 96명
for i in df.index:
    if df.loc[i,'director'] in director_B.keys():
        df.loc[i,'director_B'] += 1
df['director_C'] = 0 # director_C는 3작품 이상 7작품 미만 연출: C급, 475명
for i in df.index:
    if df.loc[i,'director'] in director_C.keys():
        df.loc[i,'director_C'] += 1

# 불필요한 column 제거
def remove_column(column):
    global df
    df = df.drop(column,axis=1)
useless = ['series','genre','actor','writer','prd_company', 'creative_type','genre_adult','genre_film-noir',
           'genre_game-show','genre_news','genre_reality-tv','genre_short','genre_talk-show','kwrds','description',
           'synop','language','country','country_1','country_2','country_3','actor_1','actor_2','actor_3','actor_4',
           'director']
remove_column(useless)


df = df.drop('index', axis = 1)

# csv로 저장
df.to_csv('../../data/cleaned/movie_meta_cleaned_ver7.csv', header=True, index=False)
