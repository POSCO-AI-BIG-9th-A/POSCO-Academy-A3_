import pandas as pd
import numpy as np


df = pd.read_csv("../../data/cleaned/movie_meta_cleaned_final2.csv", engine= "python", encoding='utf-8')

def Nan_to_point():
    global df
    for col in df.columns:
            df.loc[df[col] == '.', col] = np.nan
Nan_to_point()

# 불필요한 column 제거
def remove_column(column):
    global df
    df = df.drop(column,axis=1)
useless = ['dvd_sales','blu_sales','total_sales','release_dvd','income_opening','income_usa','income_int','income_ww',
           'dvd_over_income','APPROVED','G','NC-17','NOT RATED','PASSED','PG','PG-13','R','TV-14','TV-G','TV-MA','TV-PG',
           'TV-Y7']
remove_column(useless)


df.to_csv('../../data/cleaned/movie_meta_cleaned_final3.csv', header=True, index=False)
