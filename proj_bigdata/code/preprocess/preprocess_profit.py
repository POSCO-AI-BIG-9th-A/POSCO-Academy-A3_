import pandas as pd

df_customer = pd.read_csv("../../data/cleaned/movie_customer_cleaned.csv", engine= "python", encoding='utf-8')
df_download = pd.read_csv("../../data/cleaned/movie_download_cleaned.csv", engine= "python", encoding='utf-8')
df_price = pd.read_csv("../../data/raw/movie_price_spreadsheets.csv", engine= "python", encoding='utf-8')
df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned_ver2.csv", engine= "python", encoding='utf-8')


# 고객별 매출 'customer_sales'
rev_customer = df_download.groupby(['customer_id'])['down_price'].sum()
df_customer = pd.merge(df_customer,rev_customer, on='customer_id',how='left')
df_customer = df_customer.rename(columns={'down_price':'customer_sales'})
# 영화별 매출 'movie_down_sales'
rev_movie = df_download.groupby(['item_id'])['down_price'].sum()
df_meta = pd.merge(df_meta,rev_movie, on='item_id',how='left')
df_meta = df_meta.rename(columns={'down_price':'movie_down_sales'})

# Nan -> '.'
df_customer['customer_sales'] = df_customer['customer_sales'].fillna('.')
df_meta['movie_down_sales'] = df_meta['movie_down_sales'].fillna('.')

# inflation반영 contract_price
df_meta['contract_price_inf'] = '.'
for i in df_meta.index:
    for j in range(len(df_download['down_year'].unique())):
        if df_meta['contract_year'][i] != '.':
            if float(df_meta['contract_year'][i]) == df_download['down_year'].unique()[j]:
                df_meta['contract_price_inf'][i] = float(df_meta['contract_price'][i]) * df_download['inf_year'].unique()[j]
                print(i)

# 영화별 순수익 (contract_price를 비용으로 볼 때)
df_meta['net_profit'] = '.'
for i in df_meta.index:
    try:
        if df_meta['movie_down_sales'][i] != '.':
            df_meta.loc[i, 'net_profit'] = df_meta.loc[i, 'movie_down_sales'] - df_meta.loc[i, 'contract_price_inf']
    except:
        print('TypeError{}:'.format(i))
print('Net Profit: ${} (2018)'.format(df_meta[df_meta['net_profit'] != '.']['net_profit'].sum()))

# ROI (contract_price를 투자(즉 자산)로 볼 때)
total_revenue = df_meta[df_meta['movie_down_sales'] != '.']['movie_down_sales'].sum()  # 원래 total_net_profit이 정의에 부합하나 혼동 방지를 위해 revenue로 대체
total_investment = df_meta[df_meta['contract_price_inf'] != '.']['contract_price_inf'].sum()

ROI = float(total_revenue / total_investment) * 100
print('ROI: %.2f%%' % ROI)


df_meta.to_csv('../../data/cleaned/movie_meta_cleaned_ver3.csv', header=True, index=False)
df_customer.to_csv('../../data/cleaned/movie_customer_cleaned.csv', header=True, index=False)
