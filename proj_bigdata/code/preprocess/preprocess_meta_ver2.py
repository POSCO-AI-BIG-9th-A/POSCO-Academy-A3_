import pandas as pd

df = pd.read_csv("../../data/cleaned/movie_meta_cleaned.csv", engine= "python", encoding='utf-8')

# 불필요한 column 제거
df.drop(['index','mpa_rating_origin'],axis=1)

#한빈




#채은




#경원