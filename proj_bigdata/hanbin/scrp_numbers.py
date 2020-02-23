from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
import random
data = []

# column 생성: c1 ~ c28
for i in range(1,29):
    globals()['c{}'.format(i)] = []

f = open('/home/pirl/A3_/proj_bigdata/hanbin/movieURL_erased.txt', 'r')
tabs = f.readlines()
f.close()
f = open('error_title_1000~1999.txt', 'w')
i = 0
for tab in tabs[1000:2000]:
    try:
        i += 1
        print(i)
        url = "https://www.the-numbers.com{}".format(tab)

        resp = requests.get(url)
        html = resp.text

        soup = BeautifulSoup(html, "html5lib")


        tags_table = soup.select("#summary > table > tbody > tr > td")

        tags_dBO = soup.select("#movie_finances > tbody > tr:nth-child(2) > td.data")  # Domestic Box Office
        tags_iBO = soup.select("#movie_finances > tbody > tr:nth-child(3) > td.data.sum")  # International Box Office
        tags_wBO = soup.select("#movie_finances > tbody > tr:nth-child(4) > td.data")  # Worldwide Box Office
        tags_DVD = soup.select("#movie_finances > tbody > tr:nth-child(6) > td.data")  # Est. Domestic DVD Sales
        tags_BR = soup.select("#movie_finances > tbody > tr:nth-child(7) > td.data.sum")  # Est. Domestic Blu-ray Sales
        tags_Vdo = soup.select("#movie_finances > tbody > tr:nth-child(8) > td.data")  # Total Est. Domestic Video Sales
        tags_synop = soup.select("#summary > p:nth-child(2)")  # Synopsis

        # 'title' column(c1)
        c1.append(tab)
        print(tab, end='')

        # 'dom_bo' column(c2)
        text_dBO = ""
        for tag in tags_dBO:
            text_dBO += tag.text
        p = re.findall(r'\d+', text_dBO)
        p = ''.join(p)
        if text_dBO == '':
            c2.append('.')
        else:
            c2.append(int(p))

        # 'int_bo' column(c3)
        text_iBO = ""
        for tag in tags_iBO:
            text_iBO += tag.text
        p = re.findall(r'\d+', text_iBO)
        p = ''.join(p)
        if text_iBO == '':
            c3.append('.')
        else:
            c3.append(int(p))

        # 'wrld_bo' column(c4)
        text_wBO = ""
        for tag in tags_wBO:
            text_wBO += tag.text
        p = re.findall(r'\d+', text_wBO)
        p = ''.join(p)
        if text_wBO == '':
            c4.append('.')
        else:
            c4.append(int(p))

        # 'dvd_sales' column(c5)
        text_DVD = ""
        for tag in tags_DVD:
            text_DVD += tag.text
        p = re.findall(r'\d+', text_DVD)
        p = ''.join(p)
        if text_DVD == '':
            c5.append('.')
        else:
            c5.append(int(p))

        # 'blu_sales' column(c6)
        text_BR = ""
        for tag in tags_BR:
            text_BR += tag.text
        p = re.findall(r'\d+', text_BR)
        p = ''.join(p)
        if text_BR == '':
            c6.append('.')
        else:
            c6.append(int(p))

        # 'total_sales' column(c7)
        text_Vdo = ""
        for tag in tags_Vdo:
            text_Vdo += tag.text
        p = re.findall(r'\d+', text_Vdo)
        p = ''.join(p)
        if text_Vdo == '':
            c7.append('.')
        else:
            c7.append(int(p))

        text_k = []
        tags_k = [tags_table[i] for i in range(len(tags_table)) if i % 2 == 0]
        for tag in tags_k:
            text_k.append(tag.text)
        text_v = []
        tags_v = [tags_table[i] for i in range(len(tags_table)) if i % 2 == 1]
        for tag in tags_v:
            text_v.append(tag.text)
        if len(text_v) != len(text_k):
            f.write("len(text_v) != len(text_k) https://www.the-numbers.com{}".format(tab))
            pass
        else:
            dic = dict(zip(text_k, text_v))

            if 'Opening\xa0Weekend:' not in dic.keys():
                c8.append('.')
            if 'Running Time:' not in dic.keys():
                c28.append('.')
            if 'Legs:' not in dic.keys():
                c9.append('.')
            if 'Domestic Share:' not in dic.keys():
                c10.append('.')
            if 'Production\xa0Budget:' not in dic.keys():
                c11.append('.')
            if 'Theater counts:' not in dic.keys():
                c12.append('.')
                c13.append('.')
            if 'Infl. Adj. Dom. BO' not in dic.keys():
                c14.append('.')
            if 'Domestic Releases:' not in dic.keys():
                c26.append('.')
            if 'Video\xa0Release:' not in dic.keys():
                c15.append('.')
            if 'MPAA\xa0Rating:' not in dic.keys():
                c16.append('.')
            if 'Franchise:' not in dic.keys():
                c17.append('.')
            if 'Genre:' not in dic.keys():
                c27.append('.')
            if 'Keywords:' not in dic.keys():
                c18.append('.')
            if 'Source:' not in dic.keys():
                c19.append('.')
            if 'Production\xa0Method:' not in dic.keys():
                c20.append('.')
            if 'Creative\xa0Type:' not in dic.keys():
                c21.append('.')
            if 'Production Companies:' not in dic.keys():
                c22.append('.')
            if 'Production Countries:' not in dic.keys():
                c23.append('.')
            if 'Languages:' not in dic.keys():
                c24.append('.')

            for k, v in dic.items():

                if k == 'Opening\xa0Weekend:':
                    text_opening = v
                    p1 = re.findall(r'\d+,', text_opening)
                    p1 = re.findall(r'\d+', str(p1))
                    p2 = re.findall(r'\d+\s', text_opening)
                    p = p1 + p2
                    p = ''.join(p)
                    c8.append(int(p))

                elif k == 'Running Time:':
                    text_runtime = v
                    p = re.findall(r'\d+', text_runtime)
                    p = ''.join(p)
                    c28.append(float(p))

                elif k == 'Legs:':
                    text_Legs = v
                    p = re.findall(r'\d+.\d+|\d+\s', text_Legs)
                    p = ''.join(p)
                    c9.append(float(p))

                elif k == 'Domestic Share:':
                    text_domeShare = v
                    p = re.findall(r'\d+.\d+', text_domeShare)
                    p = ''.join(p)
                    c10.append(float(p))

                elif k == 'Production\xa0Budget:':
                    text_budget = v
                    p = re.findall(r'\d+,|\d+\s\(', text_budget)
                    p = re.findall(r'\d+', str(p))
                    p = ''.join(p)
                    c11.append(int(p))

                elif k == 'Theater counts:':
                    text_thtrCnt = v
                    p1 = re.findall(r'\d?,?\d+\sopening', text_thtrCnt)
                    p1 = re.findall(r'\d+', str(p1))
                    p2 = re.findall(r'\d?,?\d+\smax', text_thtrCnt)
                    p2 = re.findall(r'\d+', str(p2))
                    p1 = ''.join(p1)
                    c12.append(int(p1))
                    p2 = ''.join(p2)
                    c13.append(int(p2))

                elif k == 'Infl. Adj. Dom. BO':
                    text_infAdjdBO = v
                    p = re.findall(r'\d+', text_infAdjdBO)
                    p = ''.join(p)
                    c14.append(int(p))

                elif k == 'Domestic Releases:':
                    text_domRlse = v
                    p = re.findall(r'\S+\s\w+,\s\d+', text_domRlse)
                    p = ''.join(p[0])
                    c26.append(p)

                elif k == 'Video\xa0Release:':
                    text_vdRlse = v
                    p = re.findall(r'\S+\s\w+,\s\d+', text_vdRlse)
                    p = ''.join(p)
                    c15.append(p)

                elif k == 'MPAA\xa0Rating:':
                    text_MPAA = v.split(' ')
                    c16.append(text_MPAA[0])

                elif k == 'Franchise:':
                    text_Frnchs = v
                    c17.append(text_Frnchs)

                elif k == 'Genre:':
                    text_genre = dic['Genre:']
                    c27.append(text_genre.lower())

                elif k == 'Keywords:':
                    text_kwrds = v
                    c18.append(text_kwrds.lower())

                elif k == 'Source:':
                    text_src = v
                    c19.append(text_src.lower())

                elif k == 'Production\xa0Method:':
                    text_prdMthd = v
                    c20.append(text_prdMthd.lower())

                elif k == 'Creative\xa0Type:':
                    text_crtvType = v
                    c21.append(text_crtvType.lower())

                elif k == 'Production Companies:':
                    text_prdCmpny = v
                    c22.append(text_prdCmpny)

                elif k == 'Production Countries:':
                    text_prdCntry = v
                    c23.append(text_prdCntry.lower())

                elif k == 'Languages:':
                    text_lang = v
                    c24.append(text_lang.lower())

                else:
                    pass
            text_synop = ""
            for tag in tags_synop:
                text_synop += tag.text
            if text_synop == '':
                c25.append('.')
            else:
                c25.append(text_synop.lower())
    except:
        f.write("https://www.the-numbers.com{}".format(tab))
        print('error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    time.sleep(random.random()*5)

f.close()

data.append(c1); data.append(c2); data.append(c3); data.append(c4); data.append(c5); data.append(c6); data.append(c7);
data.append(c8); data.append(c28); data.append(c9); data.append(c10); data.append(c11); data.append(c12); data.append(c13);
data.append(c14); data.append(c26); data.append(c15); data.append(c16); data.append(c17); data.append(c27); data.append(c18);
data.append(c19); data.append(c20); data.append(c21); data.append(c22); data.append(c23); data.append(c24); data.append(c25)

columns = ['title','dom_bo','int_bo','wrld_bo','dvd_sales','blu_sales','total_sales',
           'opening','runtime','legs','share','budget','theater_opening', 'theater_max',
           'inf_dom_bo','release','vdo_release','mpaa','series','genre','kwrds',
           'src','prd_mthd','creative_type','prd_company','prd_country','lang','synop']
newData = dict()
for (col, d) in zip(columns, data):
    newData[col] = d
df = pd.DataFrame(newData, columns=columns)
df.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/numbers1000~1999.csv', header=True, index=False)
