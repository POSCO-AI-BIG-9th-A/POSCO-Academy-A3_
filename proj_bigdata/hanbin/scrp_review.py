import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

df = pd.read_csv('omdb_meta_merge.csv', engine='python')

num_user = []; num_critic = []

for i in range(len(df['movie_id'])):
    url = 'https://www.imdb.com/title/%s/' %list(df['movie_id'])[i]
    resp = requests.get(url)
    html = resp.text

    soup = BeautifulSoup(html,'html5lib')
    tags_user = soup.select('#title-overview-widget > div.plot_summary_wrapper > div.titleReviewBar > div.titleReviewBarItem.titleReviewbarItemBorder > div:nth-child(2) > span > a:nth-child(1)')
    tags_critic = soup.select('#title-overview-widget > div.plot_summary_wrapper > div.titleReviewBar > div.titleReviewBarItem.titleReviewbarItemBorder > div:nth-child(2) > span > a:nth-child(3)')

    text = ""
    for tag in tags_user:
        text += tag.text
    p = re.findall(r'\d+', text)
    p = ''.join(p)
    num_user.append(int(p))

    text = ""
    for tag in tags_critic:
        text += tag.text
    p = re.findall(r'\d+', text)
    p = ''.join(p)
    num_critic.append(int(p))


data = []
data.append(df['movie_id']); data.append(num_user); data.append(num_critic)

columns = ['movie_id','reviews_users','reviews_critics']
newData = dict()
for (col, d) in zip(columns, data):
    newData[col] = d
df = pd.DataFrame(newData, columns=columns)
df.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/NumOfReviews.csv', header=True, index=False)