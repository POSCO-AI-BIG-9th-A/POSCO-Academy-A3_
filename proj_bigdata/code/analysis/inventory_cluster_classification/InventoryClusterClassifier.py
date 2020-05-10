def InventoryClusterClassifier(customer_id, customer_data):
    import pandas as pd
    import pickle
    from sklearn.externals import joblib
    
    df_down_cus = pd.read_csv("./down_cust_merged.csv", engine="python")
    df_meta = pd.read_csv("./movie_meta_with_cluster.csv", engine="python")
    df_inv = df_meta[df_meta.inv_exist == 1]
    model = joblib.load("InventoryClusterClassifier.pkl")
    
    predict_cluster = model.predict(customer_data)[0]
    
    watched = list(df_down_cus[df_down_cus["customer_id"]==customer_id]["item_id"])
    
    inv_same_clus = list(set(df_inv[df_inv["cluster_kmeans"]==predict_cluster]["item_id"])-set(watched))
    
    meta_same_clus = list(df_meta[(df_meta.cluster_kmeans ==predict_cluster) & (df_meta.inv_exist==0)]["movie_id"])
    
    return predict_cluster, inv_same_clus, meta_same_clus, watched

def asso_rule_filter(inv_same_clus, watched):
    import pandas as pd
    from itertools import combinations

    asso_df = pd.read_csv("./asso_rule.csv", engine="python")

    antecedents = []
    for i in range(len(watched) + 1):
        antecedents.append(list(combinations(watched, i)))
    print(antecedents)

    consequents = []
    #     print(str(list(antecedents[1][0])) == str(asso_df.loc[11086,'antecedents']))
    for c in antecedents:
        for ids in list(c):
            for i in asso_df.index:
                if str(list(ids)) == str(asso_df.loc[i, 'antecedents']):
                    consequents.append(asso_df.loc[i, 'consequents'])
    print(consequents)

    inv_same_clus_0 = []
    inv_same_clus_1 = []
    for ids in consequents:
        for inv_ids in inv_same_clus:
            if ids == str(list(inv_ids)):
                if inv_ids in inv_same_clus_0 + inv_same_clus_1:
                    pass
                else:
                    inv_same_clus_0.append(inv_ids)
            if ids != str(list(inv_ids)):
                if inv_ids in inv_same_clus_0 + inv_same_clus_1:
                    pass
                else:
                    inv_same_clus_1.append(inv_ids)

    if inv_same_clus_0 == []:
        return inv_same_clus

    return inv_same_clus_0 + inv_same_clus_1