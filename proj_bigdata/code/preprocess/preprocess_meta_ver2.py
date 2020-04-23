import pandas as pd

df = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')

# 불필요한 column 제거
df.drop(['index','mpa_rating_origin'],axis=1)

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
