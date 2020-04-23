import pandas as pd

df = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')

# 불필요한 column 제거
df.drop(['index','mpa_rating_origin'],axis=1)

#한빈





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
