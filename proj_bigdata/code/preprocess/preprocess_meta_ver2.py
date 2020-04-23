import pandas as pd
import numpy as np

df = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')


#한빈
# 문자열로 되어 있는 숫자변수를 int, float 타입으로 변환
def string_to_numeric(df):
        col_numeric = ['release_year','runtime','imdb_score','dvd_sales','blu_sales','total_sales',
                    'legs','share','inf_income_usa','theater_opening','theater_total',
                    'metascore','big_awards_num','awards_win_num','awards_nomin_num',
                    'reviews_users','reviews_critics','budget','series_new','income_opening',
                    'votes','income_usa','income_int','income_ww']
        for col in col_numeric:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df = df.replace(np.nan, '.', regex=True)
        return df
df = string_to_numeric(df)

# Nan -> '.'
def Nan_to_point(df):
        for col in df.columns:
                df.loc[df[col].isna(), col] = '.'
        return(df)
df = Nan_to_point(df)

# 불필요한 column 제거
def remove_column(df,column):
        df = df.drop(column,axis=1)
        return df
useless = ['index','mpa_rating_origin']
remove_column(df,useless)

# Inflation 파생변수 생성
def inflation(df):
        df['inf'] = '.'
        for i in df.index:
                if (df.loc[i, 'inf_income_usa'] != '.') & (df.loc[i, 'income_usa'] != '.') & (
                        df.loc[i, 'income_usa'] != 0):
                        df.loc[i, 'inf'] = float(df.loc[i, 'inf_income_usa']) / float(df.loc[i, 'income_usa'])
                else:
                        pass
        return df
inflation(df)

# genre 더미변수 생성
# scraping 오류 수정
df.loc[df['movie_id'] == 'tt5851562', 'genre'] = 'Sci-Fi'
df.loc[df['movie_id'] == 'tt1781967', 'genre'] = 'Game-Show'
df.loc[df['movie_id'] == 'tt7048386', 'genre'] = 'Crime, Drama, Horror, Mystery, Thriller'
df.loc[df['movie_id'] == 'tt0498879', 'genre'] = 'Reality-TV'
df.loc[df['movie_id'] == 'tt4403432', 'genre'] = 'Crime'
df.loc[df['movie_id'] == 'tt2010510', 'genre'] = 'Reality-TV'

#채은




#경원