import pandas as pd

df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')

# 불필요한 column 제거
df_meta.drop(['index','mpa_rating_origin'],axis=1)

#한빈





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
    
    # dvd_over_total: 
    L=[]
    for i in range(len(df_meta)):
        if ((df_meta["dvd_sales"][i] != ".") & (df_meta["income_usa"][i] != ".")) :
            L.append(int(df_meta["dvd_sales"][i]) / int(df_meta["income_usa"][i]))
        else : L.append(".")
    
    df_meta["dvd_over_income"] = L



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
