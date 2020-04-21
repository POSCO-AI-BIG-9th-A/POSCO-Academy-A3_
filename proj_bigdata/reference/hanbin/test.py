import pandas as pd
import numpy as np

df = pd.read_csv('merged_omdb_numbers_meta_with_reviews.csv', engine='python')

# print(df.info())


print(df['movie_id'].describe())


print((0.04**2+0.36**2+0.24**2+0.26**2+0.34**2)/5)

print(0.44 + 2.776*np.sqrt(0.0744**2/5))


print((11/15)*(4/15)/150)

print(0.6*0.4/200)

print(11/15-0.6 - 1.96*np.sqrt((11/15)*(4/15)/150 + 0.6*0.4/200))

print(2.3**2/1.5**2/2.91)