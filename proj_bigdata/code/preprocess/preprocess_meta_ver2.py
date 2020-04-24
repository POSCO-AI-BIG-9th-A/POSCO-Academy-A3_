import pandas as pd
import numpy as np

df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')


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


def dvd_over_income() :
    global df_meta

    # dvd_sales 추가 정제
    for i in range(len(df_meta)) :
        try: int(df_meta["dvd_sales"][i])
        except :
            if (df_meta["dvd_sales"][i]!="."):
                if (pd.isna(df_meta["dvd_sales"][i])):
                    df_meta.loc[i,["dvd_sales"]] = "."
                else :
                    df_meta.loc[i,["dvd_sales"]] = df_meta["dvd_sales"][i].replace(",", "")

        #상엽코드 추가
        movie_id = df_meta["movie_id"][i]
        if movie_id == "tt2349460":
            # Grace Unplugged
            df_meta.loc[i,"dvd_sales"] = "3980659"
            df_meta.loc[i,"blu_sales"] = "536454"
            df_meta.loc[i,"total_sales"] = "4517113"

        if movie_id == "tt0790804":
            # The Comebacks
            df_meta.loc[i,"dvd_sales"] = "9421539"
            df_meta.loc[i,"blu_sales"] = "."
            df_meta.loc[i,"total_sales"] = "9421539"

        if movie_id == "tt0478304":
            # The Tree of Life (2011)
            df_meta.loc[i,"dvd_sales"] = "."
            df_meta.loc[i,"blu_sales"] = "5535861"
            df_meta.loc[i,"total_sales"] = "5535861"

        if movie_id == "tt8688634":
            # 21 Bridges (2019)
            df_meta.loc[i,"dvd_sales"] = "562041"
            df_meta.loc[i,"blu_sales"] = "981911"
            df_meta.loc[i,"total_sales"] = "1543952"    
    
    # dvd_over_total: 
    L=[]
    for i in range(len(df_meta)):
        if ((df_meta["dvd_sales"][i] != ".") & (df_meta["income_usa"][i] != ".")) :
            L.append(int(df_meta["dvd_sales"][i]) / int(df_meta["income_usa"][i]))
        else : L.append(".")

    df_meta["dvd_over_income"] = L

dvd_over_income()


#경원

# raw/inv에서 meta로 옮기기
def inv_to_meta():
    global df_meta

    df_meta_raw = pd.read_csv('../../data/raw/spreadsheet/movie_meta_spreadsheets.csv', engine='python',encoding="utf-8")
    df_inv = pd.read_csv('../../data/raw/movie_inventory_spreadsheets.csv', engine='python', encoding="utf-8")

    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt2072227"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt1391871"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt1266072"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt0488888"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt1664697"].index)

    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt4380070"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt4982758"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt1014762"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt0290983"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt2367359"].index)

    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt0485877"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt7017420"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt3075362"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt1095453"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt1663702"].index)

    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt3462264"].index)
    df_meta_raw = df_meta_raw.drop(df_meta_raw[df_meta_raw["movie_id"] == "tt4836716"].index)

    df_meta_raw = df_meta_raw.reset_index(drop=False, inplace=False)

    # meta_ raw의 contract_price/studio_score/price_class -> meta로 옮기기
    for i in range(len(df_meta_raw)):
        meta_mId = df_meta_raw["movie_id"][i]

        # contract_price / studio_score / price_class
        df_meta.loc[(df_meta["movie_id"] == meta_mId), "contract_price"] = df_meta_raw["contract_price"][i]
        df_meta.loc[(df_meta["movie_id"] == meta_mId), "studio_score"] = df_meta_raw["studio_score"][i]
        df_meta.loc[(df_meta["movie_id"] == meta_mId), "price_class"] = df_meta_raw["price_class"][i]

    df_meta["item_id"] = "."
    df_meta["inv_exist"] = 0
    df_meta["contract_year"] = "."

    for i in range(len(df_meta)):
        for j in range(len(df_inv)):
            if df_meta["movie_id"][i] == df_inv["movie_id"][j]:
                meta_mId = df_meta["movie_id"][i]

                # item_id 옮기기
                df_meta.loc[(df_meta["movie_id"] == meta_mId), "item_id"] = df_inv["item_id"][j]

                # inv_exist(inv에 데이터가 존재하면 1, 아니면 0으로 표시)
                df_meta.loc[(df_meta["movie_id"] == meta_mId), "inv_exist"] = 1

                # contract_year 옮기기
                df_meta.loc[(df_meta["movie_id"] == meta_mId), "contract_year"] = df_inv["contract_year"][j]

# inv_to_meta()
