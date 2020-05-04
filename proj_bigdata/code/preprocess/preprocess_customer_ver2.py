import pandas as pd

df_customer = pd.read_csv("../../data/cleaned/movie_customer_cleaned_ver2.csv",engine="python", encoding='utf-8')
df_download = pd.read_csv("../../data/cleaned/movie_download_cleaned.csv", engine= "python", encoding='utf-8')
cust_cluster_nums = pd.read_csv("../../data/analysis/customer_cluster_nums.csv", engine="python", encoding='utf-8')

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


def cust_cluster_num_columns():
    global df_customer
    global cust_cluster_nums

    df_customer = pd.merge(df_customer, cust_cluster_nums, left_index=True, right_index=True, how="left")

cust_cluster_num_columns()

df_customer.to_csv("../../data/cleaned/movie_customer_cleaned_ver3.csv", header=True, index=False)