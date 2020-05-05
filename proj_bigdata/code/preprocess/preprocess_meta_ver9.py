import pandas as pd

df_meta = pd.read_csv('../../data/cleaned/movie_meta_cleaned_final2.csv', engine='python', encoding="utf-8")

def release_dvd_addition():
    global df_meta
    df_meta.loc[df_meta.movie_id == "tt1477834", "release_dvd"] = '26-03-2019'
    df_meta.loc[df_meta.movie_id == "tt5028340", "release_dvd"] = '19-03-2019'
    df_meta.loc[df_meta.movie_id == "tt0405469", "release_dvd"] = '12-09-2006'
    df_meta.loc[df_meta.movie_id == "tt4575576", "release_dvd"] = '06-11-2018'
    df_meta.loc[df_meta.movie_id == "tt2822672", "release_dvd"] = '23-05-2017'
    df_meta.loc[df_meta.movie_id == "tt1232200", "release_dvd"] = '16-10-2012'
    df_meta.loc[df_meta.movie_id == "tt0462322", "release_dvd"] = '18-09-2007'
    df_meta.loc[df_meta.movie_id == "tt0120768", "release_dvd"] = '30-06-2009'
    df_meta.loc[df_meta.movie_id == "tt0279889", "release_dvd"] = '03-01-2012'
    df_meta.loc[df_meta.movie_id == "tt0385726", "release_dvd"] = '06-06-2006'
    df_meta.loc[df_meta.movie_id == "tt2328900", "release_dvd"] = '26-02-2019'
    df_meta.loc[df_meta.movie_id == "tt1893256", "release_dvd"] = '24-09-2013'  # 20
    df_meta.loc[df_meta.movie_id == "tt0795368", "release_dvd"] = '26-12-2008'
    df_meta.loc[df_meta.movie_id == "tt8097306", "release_dvd"] = '12-02-2019'
    df_meta.loc[df_meta.movie_id == "tt7690670", "release_dvd"] = '11-09-2018'  # 30
    df_meta.loc[df_meta.movie_id == "tt7125860", "release_dvd"] = '26-03-2019'
    df_meta.loc[df_meta.movie_id == "tt5301662", "release_dvd"] = '09-01-2018'
    df_meta.loc[df_meta.movie_id == "tt1502407", "release_dvd"] = '15-01-2019'
    df_meta.loc[df_meta.movie_id == "tt4595882", "release_dvd"] = '19-02-2019'
    df_meta.loc[df_meta.movie_id == "tt2553908", "release_dvd"] = '15-10-2013'  # 40

    df_meta.loc[df_meta.movie_id == "tt7961060", "release_dvd"] = '16-04-2019'
    df_meta.loc[df_meta.movie_id == "tt5727282", "release_dvd"] = '03-07-2018'
    df_meta.loc[df_meta.movie_id == "tt2918436", "release_dvd"] = '16-06-2015'
    df_meta.loc[df_meta.movie_id == "tt0090655", "release_dvd"] = '21-03-2013'
    df_meta.loc[df_meta.movie_id == "tt3216348", "release_dvd"] = '07-03-2017'  # 50

    df_meta.loc[df_meta.movie_id == "tt5804314", "release_dvd"] = '27-02-2018'
    df_meta.loc[df_meta.movie_id == "tt6512428", "release_dvd"] = '29-01-2019'
    df_meta.loc[df_meta.movie_id == "tt1634003", "release_dvd"] = '19-07-2016'
    df_meta.loc[df_meta.movie_id == "tt6288250", "release_dvd"] = '07-11-2017'  # 60

    df_meta.loc[df_meta.movie_id == "tt0390521", "release_dvd"] = '28-09-2004'  # 70

    df_meta.loc[df_meta.movie_id == "tt0388482", "release_dvd"] = '10-01-2006'
    df_meta.loc[df_meta.movie_id == "tt2625810", "release_dvd"] = '04-10-2016'
    df_meta.loc[df_meta.movie_id == "tt4721124", "release_dvd"] = '08-08-2017'
    df_meta.loc[df_meta.movie_id == "tt6902696", "release_dvd"] = '04-06-2019'
    df_meta.loc[df_meta.movie_id == "tt2101383", "release_dvd"] = '21-06-2016'
    df_meta.loc[df_meta.movie_id == "tt2488778", "release_dvd"] = '02-02-2016'  # 80

    df_meta.loc[df_meta.movie_id == "tt2639336", "release_dvd"] = '28-03-2019'
    df_meta.loc[df_meta.movie_id == "tt2056771", "release_dvd"] = '06-09-2016'
    df_meta.loc[df_meta.movie_id == "tt5669936", "release_dvd"] = '26-12-2017'  # 100

    df_meta.loc[df_meta.movie_id == "tt0491175", "release_dvd"] = '06-02-2018'
    df_meta.loc[df_meta.movie_id == "tt0460890", "release_dvd"] = '17-04-2018'
    df_meta.loc[df_meta.movie_id == "tt5628302", "release_dvd"] = '04-09-2018'
    df_meta.loc[df_meta.movie_id == "tt2515030", "release_dvd"] = '06-10-2015'  # 110

    df_meta.loc[df_meta.movie_id == "tt0790770", "release_dvd"] = '19-07-2016'
    df_meta.loc[df_meta.movie_id == "tt1490785", "release_dvd"] = '05-07-2016'
    df_meta.loc[df_meta.movie_id == "tt3072482", "release_dvd"] = '26-07-2016'
    df_meta.loc[df_meta.movie_id == "tt1987680", "release_dvd"] = '21-05-2019'  # 120

    df_meta.loc[df_meta.movie_id == "tt4468740", "release_dvd"] = '24-07-2018'

release_dvd_addition()

def new_dvd_col():
    L = []
    for i in range(len(df_meta)):
        if df_meta["release_dvd"][i] == ".": L.append(0)
        else : L.append(1)

    df_meta["dvd"] = L

new_dvd_col()

df_meta.to_csv('../../data/cleaned/movie_meta_cleaned_final3.csv', header=True, index=False)
