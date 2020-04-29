import pandas as pd

df_download = pd.read_csv("../../data/raw/movie_download_spreadsheets.csv", engine= "python", encoding='utf-8')
df_price = pd.read_csv("../../data/raw/movie_price_spreadsheets.csv", engine= "python", encoding='utf-8')

# 연도별 인플레이션(2018년도 가치로 환산) https://www.usinflationcalculator.com/inflation/current-inflation-rates/
df_download['down_year'].describe()
df_download.loc[df_download['down_year'] == 2014, 'inf_year'] = 1.021 *1.013 * 1.001 * 1.016
df_download.loc[df_download['down_year'] == 2015, 'inf_year'] = 1.021 *1.013 * 1.001
df_download.loc[df_download['down_year'] == 2016, 'inf_year'] = 1.021 *1.013
df_download.loc[df_download['down_year'] == 2017, 'inf_year'] = 1.021
df_download.loc[df_download['down_year'] == 2018, 'inf_year'] = 1

# down_price = subscribe_price(해당 연도,해당 item) * inf_year (다운받은 시점의 영화가격을  2018년 기준으로 환산)
for i in df_download.index:
    print(i)
    for j in df_price.index:
        if (df_download.loc[i,'down_year'] == df_price.loc[j,'price_year']) & (df_download.loc[i,'item_id'] == df_price.loc[j,'item_id']):
            df_download.loc[i,'down_price'] = df_price.loc[j,'subscribe_price'] * df_download.loc[i,'inf_year']
        else:
            pass

df_download = df_download[df_download['down_price'].isna() == False]
df_download = df_download.reset_index().drop('index', axis=1)

df_download.to_csv('../../data/cleaned/movie_download_cleaned.csv', header=True, index=False)
