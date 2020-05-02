import pandas as pd

# Add Sentiment Infomation (positive_probability) by KoYo
def AddSentimentInfo(df):
    df_sentiment = pd.read_csv("../../data/raw/sentiment/movie_meta_sentiment.csv", engine="python", encoding="utf-8")
    df_sentiment.drop(columns=['title','result'], inplace=True)
    return df.merge(df_sentiment, on="movie_id")

if __name__ == "__main__":
    df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned_ver5.csv", engine="python", encoding="utf-8")
    df_meta = AddSentimentInfo(df_meta)
    df_meta.to_csv("../../data/cleaned/movie_meta_cleaned_ver6.csv", header=True, index=False)
    print("Done")


