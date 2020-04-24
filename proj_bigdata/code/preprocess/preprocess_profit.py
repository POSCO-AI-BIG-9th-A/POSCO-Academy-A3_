import pandas as pd

df_customer = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/cleaned/movie_customer_cleaned.csv", engine= "python", encoding='utf-8')
df_download = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/cleaned/movie_download_raw.csv", engine= "python", encoding='utf-8')
df_price = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/cleaned/movie_price_raw.csv", engine= "python", encoding='utf-8')

# 연도별 인플레이션(2018년도 가치로 환산) https://www.usinflationcalculator.com/inflation/current-inflation-rates/
df_download['down_year'].describe()
df_download.loc[df_download['down_year'] == 2014, 'inf_year'] = 1.021 *1.013 * 1.001 * 1.016
df_download.loc[df_download['down_year'] == 2015, 'inf_year'] = 1.021 *1.013 * 1.001
df_download.loc[df_download['down_year'] == 2016, 'inf_year'] = 1.021 *1.013
df_download.loc[df_download['down_year'] == 2017, 'inf_year'] = 1.021
df_download.loc[df_download['down_year'] == 2018, 'inf_year'] = 1

