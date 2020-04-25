import pandas as pd

df_customer = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/cleaned/movie_customer_cleaned.csv", engine= "python", encoding='utf-8')
df_download = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/raw/movie_download_spreadsheets.csv", engine= "python", encoding='utf-8')
df_price = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/raw/movie_price_spreadsheets.csv", engine= "python", encoding='utf-8')
df_meta = pd.read_csv("C:/Users/cresc/PycharmProjects/POSCO-Academy-A3_/proj_bigdata/data/cleaned/movie_meta_cleaned_ver2.csv", engine= "python", encoding='utf-8')

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

# 고객별 매출 'customer_sales'
rev_customer = df_download.groupby(['customer_id'])['down_price'].sum()
df_customer = pd.merge(df_customer,rev_customer, on='customer_id',how='left')
df_customer = df_customer.rename(columns={'down_price':'customer_sales'})
# 영화별 매출 'movie_down_sales'
rev_movie = df_download.groupby(['item_id'])['down_price'].sum()
df_meta = pd.merge(df_meta,rev_movie, on='item_id',how='left')
df_meta = df_meta.rename(columns={'down_price':'movie_down_sales'})

# inflation반영 contract_price
df_meta['contract_price_inf'] = '.'
for i in df_meta.index:
    for j in range(len(df_download['down_year'].unique())):
        if df_meta['contract_year'][i] == df_download['down_year'].unique()[j]:
            df_meta['contract_price_inf'][i] = float(df_meta['contract_price'][i]) * df_download['inf_year'].unique()[j]
            print(i)

# 영화별 순수익 (contract_price를 비용으로 볼 때)
df_meta['net_profit'] = '.'
for i in df_meta.index:
    if df_meta['movie_down_sales'][i] != '.':
        df_meta['net_profit'][i] = df_meta['movie_down_sales'][i] - df_meta['contract_price_inf'][i]

print('Net Profit: ${} (2018)'.format(df_meta[df_meta['net_profit'] != '.']['net_profit'].sum()))

# ROI (contract_price를 투자(즉 자산)로 볼 때)
total_revenue = df_meta[df_meta['movie_down_sales'] != '.'][
    'movie_down_sales'].sum()  # 원래 total_net_profit이 정의에 부합하나 혼동 방지를 위해 revenue로 대체
total_investment = df_meta[df_meta['contract_price_inf'] != '.']['contract_price_inf'].sum()
ROI = float(total_revenue / total_investment) * 100
print('ROI: %.2f%%' % ROI)