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
