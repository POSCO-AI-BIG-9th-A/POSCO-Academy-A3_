import pandas as pd
import numpy as np

# final ver5 생성파일입니다.
# votes 와 income들의 생성값이 이상하여 수정하였습니다.
def modifyData(df):
    # income 수정
    df.loc[df['movie_id'] == 'tt0889583', ['income_usa', 'income_int', 'income_ww']] = [60054530.0, 78653997.0,
                                                                                        138708527.0]
    df.loc[df['movie_id'] == 'tt0081400', ['income_usa', 'income_int', 'income_ww']] = [7000000.0, 0.0, 7000000.0]
    df.loc[df['movie_id'] == 'tt0472198', ['income_usa', 'income_int', 'income_ww']] = [36843682.0, 8128501.0,
                                                                                        44972183.0]
    df.loc[df['movie_id'] == 'tt1007018', ['income_usa', 'income_int', 'income_ww']] = [19716.0, 0.0, 19716.0]
    df.loc[df['movie_id'] == 'tt1210071', ['income_usa', 'income_int', 'income_ww']] = [0.0, 0.0, 0.0]
    df.loc[df['movie_id'] == 'tt0066769', ['income_usa', 'income_int', 'income_ww']] = [12376563.0, 0.0, 12376563.0]
    df.loc[df['movie_id'] == 'tt0046183', ['income_usa', 'income_int', 'income_ww']] = [87400000.0, 0.0, 87400000.0]
    df.loc[df['movie_id'] == 'tt4103724', ['income_usa', 'income_int', 'income_ww']] = [16376066.0, 0.0, 16376066.0]
    df.loc[df['movie_id'] == 'tt4700756', ['income_usa', 'income_int', 'income_ww']] = [890303.0, 0.0, 890303.0]
    df.loc[df['movie_id'] == 'tt0083739', ['income_usa', 'income_int', 'income_ww']] = [6965361.0, 0.0, 6965361.0]
    df.loc[df['movie_id'] == 'tt0053793', ['income_usa', 'income_int', 'income_ww']] = [10400000.0, 0.0, 10400000.0]
    df.loc[df['movie_id'] == 'tt0094118', ['income_usa', 'income_int', 'income_ww']] = [7888000.0, 0.0, 7888000.0]
    df.loc[df['movie_id'] == 'tt0078872', ['income_usa', 'income_int', 'income_ww']] = [37799643.0, 0.0, 37799643.0]
    df.loc[df['movie_id'] == 'tt2247692', ['income_usa', 'income_int', 'income_ww']] = [33349941.0, 0.0, 33349941.0]
    df.loc[df['movie_id'] == 'tt0056592', ['income_usa', 'income_int', 'income_ww']] = [13129846.0, 0.0, 13129846.0]
    df.loc[df['movie_id'] == 'tt0118789', ['income_usa', 'income_int', 'income_ww']] = [2380606.0, 0.0, 2380606.0]
    df.loc[df['movie_id'] == 'tt2051894', ['income_usa', 'income_int', 'income_ww']] = [2859955.0, 0.0, 2859955.0]
    df.loc[df['movie_id'] == 'tt0057590', ['income_usa', 'income_int', 'income_ww']] = [37600000.0, 0.0, 37600000.0]
    df.loc[df['movie_id'] == 'tt4191580', ['income_usa', 'income_int', 'income_ww']] = [9097072.0, 0.0, 9097072.0]
    df.loc[df['movie_id'] == 'tt0451176', ['income_usa', 'income_int', 'income_ww']] = [1692693.0, 1104506.0, 2797199.0]
    df.loc[df['movie_id'] == 'tt1211890', ['income_usa', 'income_int', 'income_ww']] = [236806.0, 0.0, 236806.0]
    df.loc[df['movie_id'] == 'tt0780595', ['income_usa', 'income_int', 'income_ww']] = [6881021.0, 0.0, 6881021.0]
    df.loc[df['movie_id'] == 'tt5208252', ['income_usa', 'income_int', 'income_ww']] = [17612099.0, 0.0, 17612099.0]
    df.loc[df['movie_id'] == 'tt0395495', ['income_usa', 'income_int', 'income_ww']] = [15432542.0, 0.0, 15432542.0]
    df.loc[df['movie_id'] == 'tt0082801', ['income_usa', 'income_int', 'income_ww']] = [29916207.0, 0.0, 29916207.0]
    df.loc[df['movie_id'] == 'tt6588966', ['income_usa', 'income_int', 'income_ww']] = [0.0, 30444106.0, 30444106.0]

    # inf 재적용 , share 수정
    for idx in df.index:
        # inf
        inf_value = df.loc[idx, "inf"]
        inf_lst = [x*inf_value for x in df.loc[idx, ["income_usa", "income_int", "income_ww"]].values]
        df.loc[idx, ["inf_income_usa", "inf_income_int", "inf_income_ww"]] = inf_lst
        # share
        (usa, ww) = zip(df.loc[idx, ["inf_income_usa", "inf_income_ww"]].values)
        if ww[0] == 0.0:
            df.loc[idx, "share"] = 0.0
        else:
            df.loc[idx, "share"] = usa[0] / ww[0] * 100
        # print(usa[0] / ww[0] * 100)

    # vote 수정
    df.loc[df['movie_id'] == 'tt0889583', 'votes'] = 136638.0
    df.loc[df['movie_id'] == 'tt1179258', 'votes'] = 10155.0



if __name__ == "__main__":
    df = pd.read_csv("../../data/cleaned/movie_meta_cleaned_final4.csv", encoding="utf-8", engine="python")
    modifyData(df)
    df.to_csv("../../data/cleaned/movie_meta_cleaned_final5.csv", header=True, index=False)
    print("done")