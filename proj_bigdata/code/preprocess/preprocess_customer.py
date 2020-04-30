import pandas as pd

df_customer = pd.read_csv("../../data/raw/modified_by_dayeon/movie_customer_new.csv", engine = "python")
df_download = pd.read_csv("../../data/raw/movie_download_spreadsheets.csv", engine = "python")

#채은
def cust_preprocess():
    import pandas as pd
    global df_customer
    global df_download

    last_down = []
    for x in df_customer["customer_id"]:
        try:
            last_date = max(df_download[df_download["customer_id"] == x]["down_date"])
            last_down.append(last_date)
        except:
            last_down.append(".")

    down_flag = [0 if x=='.' else 1 for x in last_down]

    df_customer["last_down_date"] = last_down
    df_customer["down_flag"] = down_flag

cust_preprocess()


def freq_down_weekday():
    import numpy as np
    global df_customer
    global df_download

    L = []
    for x in df_customer["customer_id"]:
        weekdays = list(df_download[df_download["customer_id"] == x]["weekday"])
        if len(weekdays) > 0:
            L.append(np.bincount(weekdays).argmax())
        else:
            L.append(".")

    df_customer["freq_down_weekday"] = L

freq_down_weekday()

df_customer.to_csv("../../data/cleaned/movie_customer_cleaned_ver3.csv", header=True, index=False)
