import pandas as pd
import numpy as np

df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')


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
inv_to_meta()

#한빈
# 문자열로 되어 있는 숫자변수를 int, float 타입으로 변환
def string_to_numeric(col_numeric):
        global df_meta
        for col in col_numeric:
            df_meta[col] = pd.to_numeric(df_meta[col], errors='coerce')
            df_meta = df_meta.replace(np.nan, '.', regex=True)
col_numeric = ['release_year', 'runtime', 'imdb_score', 'dvd_sales', 'blu_sales', 'total_sales',
               'legs', 'share', 'inf_income_usa', 'theater_opening', 'theater_total',
               'metascore', 'big_awards_num', 'awards_win_num', 'awards_nomin_num',
               'reviews_users', 'reviews_critics', 'budget', 'series_new', 'income_opening',
               'votes', 'income_usa', 'income_int', 'income_ww', 'contract_price', 'studio_score', 'price_class','contract_year']
string_to_numeric(col_numeric)

# 불필요한 column 제거
def remove_column(column):
    global df_meta
    df_meta = df_meta.drop(column,axis=1)
useless = ['index', 'mpa_rating_origin']
remove_column(useless)

# Inflation 파생변수 생성
def inflation():
    global df_meta
    df_meta['inf'] = '.'
    for i in df_meta.index:
            if (df_meta.loc[i, 'inf_income_usa'] != '.') & (df_meta.loc[i, 'income_usa'] != '.') & (
                    df_meta.loc[i, 'income_usa'] != 0):
                    df_meta.loc[i, 'inf'] = float(df_meta.loc[i, 'inf_income_usa']) / float(df_meta.loc[i, 'income_usa'])
            else:
                    pass
inflation()

# genre 더미변수 생성
def genre_get_dummies():
    global df_meta
    # scraping 오류 수정
    df_meta.loc[df_meta['movie_id'] == 'tt5851562', 'genre'] = 'Sci-Fi'
    df_meta.loc[df_meta['movie_id'] == 'tt1781967', 'genre'] = 'Game-Show'
    df_meta.loc[df_meta['movie_id'] == 'tt7048386', 'genre'] = 'Crime, Drama, Horror, Mystery, Thriller'
    df_meta.loc[df_meta['movie_id'] == 'tt0498879', 'genre'] = 'Reality-TV'
    df_meta.loc[df_meta['movie_id'] == 'tt4403432', 'genre'] = 'Crime'
    df_meta.loc[df_meta['movie_id'] == 'tt2010510', 'genre'] = 'Reality-TV'
    df_meta.loc[df_meta['movie_id'] == 'tt4950016', 'genre'] = 'Comedy'
    # 전체 장르 목록 구하기
    genre_list = []
    for i in df_meta.index:
        genre = df_meta.loc[i,'genre'].split(',')
        for g in genre:
            g = g.strip().lower()
            if g not in genre_list:
                genre_list.append(g)
    genre_list.remove('.')
    # 각 장르별 더미 변수 만들기
    for i in df_meta.index:
        genre_0 = df_meta.loc[i,'genre'].split(',')
        genre_1 = []
        for g in genre_0:
            g = g.strip().lower()
            genre_1.append(g)
        for g in genre_list:
            if g in genre_1:
                df_meta.loc[i,'genre_{}'.format(g)] = 1
            else:
                df_meta.loc[i,'genre_{}'.format(g)] = 0
genre_get_dummies()

# country 변수 1,2,3로 쪼개기
def country():
    global df_meta
    df_meta['country_1'] = df_meta['country'].str.split(',').str[0]
    df_meta['country_2'] = df_meta['country'].str.split(',').str[1]
    df_meta['country_3'] = df_meta['country'].str.split(',').str[2]
    df_meta['country_1'].str.strip()
    df_meta['country_2'].str.strip()
    df_meta['country_3'].str.strip()
country()

# Nan -> '.'
def Nan_to_point():
    global df_meta
    for col in df_meta.columns:
            df_meta.loc[df_meta[col].isna(), col] = '.'
Nan_to_point()

#채은
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

# 결측치 14개 이상인 관측치 삭제
def tm_nan_row_drop():
    global df_meta
    nancount = []
    for i in df_meta.index:
        count = 0
        consider_columns = ["movie_id", "title", "release_year", "runtime", "mpa_rating", "imdb_score", "dvd_sales",
                            "blu_sales", "total_sales",
                            "legs", "share", "inf_income_usa", "theater_opening", "theater_total", "src",
                            "creative_type", "director", "actor", "writer",
                            "description", "synop", "awards", "poster", "metascore", "release_dvd", "genre", "country",
                            "language", "budget", "kwrds",
                            "income_opening", "votes", "income_usa", "income_int", "income_ww", "poster",
                            "reviews_users", "reviews_critics", "prd_mthd",
                            "prd_company", "release_date"]
        # 삭제예정 컬럼 불포함 : mpa_rating_origin, series 불포함
        # 파생변수/더미변수 불포함 : big_awards_num, awards_win_num, awards_nomin_num, series_new, actor_1, actor_2, actor_3, actor_4
        # 교수님이 임의추가한 세변수 불포함 : contract_price, studio_score, price_class
        for c in consider_columns:

            if df_meta[c][i] == ".":
                count += 1
        if count >= 14: nancount.append(i)
    print(str(len(nancount)) + "개 관측치 삭제")
    for i in nancount:
        df_meta = df_meta.drop(i, 0)
    print("제거 후 관측치 " + str(len(df_meta)) + "개")
tm_nan_row_drop()

df_meta.to_csv('../../data/cleaned/movie_meta_cleaned_ver2.csv', header=True, index=False)



