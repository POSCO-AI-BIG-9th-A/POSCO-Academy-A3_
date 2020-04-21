import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

data = []

# column 생성: c1 ~ c24
for i in range(1,25):
    globals()['c{}'.format(i)] = []

f = open('/home/pirl/A3_/proj_bigdata/hanbin/movieURL.txt', 'r')
tabs = f.readlines()
f.close()
for tab in tabs[0:10]:
    url = "https://www.the-numbers.com{}".format(tab)
    resp = requests.get(url)
    html = resp.text

    soup = BeautifulSoup(html, "html5lib")

    tags_synop = soup.select("#summary > p:nth-child(2)") # Synopsis
    tags_dBO = soup.select("#movie_finances > tbody > tr:nth-child(2) > td.data") # Domestic Box Office
    tags_iBO = soup.select("#movie_finances > tbody > tr:nth-child(3) > td.data.sum") # International Box Office
    tags_wBO = soup.select("#movie_finances > tbody > tr:nth-child(4) > td.data") # Worldwide Box Office
    tags_DVD = soup.select("#movie_finances > tbody > tr:nth-child(6) > td.data") # Est. Domestic DVD Sales
    tags_BR = soup.select("#movie_finances > tbody > tr:nth-child(7) > td.data.sum") # Est. Domestic Blu-ray Sales
    tags_Vdo = soup.select("#movie_finances > tbody > tr:nth-child(8) > td.data") # Total Est. Domestic Video Sales
    tags_opening = soup.select("#summary > table:nth-child(6) > tbody > tr:nth-child(1) > td:nth-child(2)") # Opening Weekend Box Office
    tags_Legs = soup.select("#summary > table:nth-child(6) > tbody > tr:nth-child(2) > td:nth-child(2)") # Legs: domestic box office/biggest weekend
    tags_domeShare = soup.select("#summary > table:nth-child(6) > tbody > tr:nth-child(3) > td:nth-child(2)") # Domestic Share: domestic box office/worldwide
    tags_budget = soup.select("#summary > table:nth-child(6) > tbody > tr:nth-child(4) > td:nth-child(2)") # Production Budget
    tags_thtrCnt = soup.select("#summary > table:nth-child(6) > tbody > tr:nth-child(5) > td:nth-child(2)") # Theater counts: opening theaters/ max.theater
    tags_infAdjdBO = soup.select("#summary > table:nth-child(6) > tbody > tr:nth-child(6) > td:nth-child(2)") # Inflation adjusted domestic Box Office
    tags_vdRlse = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(3) > td:nth-child(2)") # Video Release
    tags_MPAA = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(4) > td:nth-child(2)") # MPAA Rating
    tags_Frnchs = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(6) > td:nth-child(2)") # Franchise
    tags_kwrds = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(8) > td:nth-child(2)") # Keywords
    tags_src = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(9) > td:nth-child(2)") # Source(원작)
    tags_prdMthd = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(11) > td:nth-child(2)") # Production Method
    tags_crtvType = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(12) > td:nth-child(2)") # Creative Type
    tags_prdCmpny = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(13) > td:nth-child(2)") # Production Companies
    tags_prdCntry = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(14) > td:nth-child(2)") # Production Countries
    tags_lang = soup.select("#summary > table:nth-child(12) > tbody > tr:nth-child(15) > td:nth-child(2)") # Languages

    # 'dom_bo' column(c2)
    text_dBO = ""
    for tag in tags_dBO:
        text_dBO += tag.text
    p = re.findall(r'\d+', text_dBO)
    p = ''.join(p)
    c2.append(int(p))

    # 'int_bo' column(c3)
    text_iBO = ""
    for tag in tags_iBO:
        text_iBO += tag.text
    p = re.findall(r'\d+', text_iBO)
    p = ''.join(p)
    c3.append(int(p))

    # 'wrld_bo' column(c4)
    text_wBO = ""
    for tag in tags_wBO:
        text_wBO += tag.text
    p = re.findall(r'\d+', text_wBO)
    p = ''.join(p)
    c4.append(int(p))

    # 'dvd_sales' column(c5)
    text_DVD = ""
    for tag in tags_DVD:
        text_DVD += tag.text
    p = re.findall(r'\d+', text_DVD)
    p = ''.join(p)
    c5.append(int(p))

    # 'blu_sales' column(c6)
    text_BR = ""
    for tag in tags_BR:
        text_BR += tag.text
    p = re.findall(r'\d+', text_BR)
    p = ''.join(p)
    c6.append(int(p))

    # 'total_sales' column(c7)
    text_Vdo = ""
    for tag in tags_Vdo:
        text_Vdo += tag.text
    p = re.findall(r'\d+', text_Vdo)
    p = ''.join(p)
    c7.append(int(p))

    # 'opening' column(c8)
    text_opening = ""
    for tag in tags_opening:
        text_opening += tag.text
    p1 = re.findall(r'\d+,', text_opening)
    p1 = re.findall(r'\d+', str(p1))
    p2 = re.findall(r'\d+\s', text_opening)
    p = p1 + p2
    p = ''.join(p)
    c8.append(int(p))

    #'legs' column(c9)
    text_Legs = ""
    for tag in tags_Legs:
        text_Legs += tag.text
    p = re.findall(r'\d+.\d+|\d+\s', text_Legs)
    p = ''.join(p)
    c9.append(float(p))

    #'share' column(c10)
    text_domeShare = ""
    for tag in tags_domeShare:
        text_domeShare += tag.text
    p = re.findall(r'\d+.\d+', text_domeShare)
    p = ''.join(p)
    c10.append(float(p))

    #'budget' column(c11)
    text_budget = ""
    for tag in tags_budget:
        text_budget += tag.text
    p = re.findall(r'\d+', text_budget)
    p = ''.join(p)
    c11.append(int(p))

    #'theater_cnts' column(c12)
    #'theater_max' column(c13)
    text_thtrCnt = ""
    for tag in tags_thtrCnt:
        text_thtrCnt += tag.text
    p1 = re.findall(r'\d?,?\d+\sopening', text_thtrCnt)
    p1 = re.findall(r'\d+', str(p1))
    p2 = re.findall(r'\d?,?\d+\smax', text_thtrCnt)
    p2 = re.findall(r'\d+', str(p2))
    p1 = ''.join(p1)
    c12.append(int(p1))
    p2 = ''.join(p2)
    c13.append(int(p2))

    #'inf_dom_bo' column(c14)
    text_infAdjdBO = ""
    for tag in tags_infAdjdBO:
        text_infAdjdBO += tag.text
    p = re.findall(r'\d+', text_infAdjdBO)
    p = ''.join(p)
    c14.append(int(p))

    #'vdo_release' column(c15)
    text_vdRlse = ""
    for tag in tags_vdRlse:
        text_vdRlse += tag.text
    p = re.findall(r'\S+\s\w+,\s\d+', text_vdRlse)
    p = ''.join(p)
    c15.append(p)

    #'mpaa' column(c16)
    text_MPAA = ""
    for tag in tags_MPAA:
        text_MPAA += tag.text
    text_MPAA = text_MPAA.split(' ')
    c16.append(text_MPAA[0])

    #'series' column(c17)
    text_Frnchs = ""
    for tag in tags_Frnchs:
        text_Frnchs += tag.text
    c17.append(text_Frnchs)

    #'kwrds' column(c18)
    text_kwrds = ""
    for tag in tags_kwrds:
        text_kwrds += tag.text
    c18.append(text_kwrds.lower())

    #'src' column(c19)
    text_src = ""
    for tag in tags_src:
        text_src += tag.text
    c19.append(text_src.lower())

    #'prd_mthd' column(c20)
    text_prdMthd = ""
    for tag in tags_prdMthd:
        text_prdMthd += tag.text
    c20.append(text_prdMthd.lower())

    #'creative_type' column(c21)
    text_crtvType = ""
    for tag in tags_crtvType:
        text_crtvType += tag.text
    c21.append(text_crtvType.lower())

    #'prd_company' column(c22)
    text_prdCmpny = ""
    for tag in tags_prdCmpny:
        text_prdCmpny += tag.text
    c22.append(text_prdCmpny)

    #'prd_country' column(c23)
    text_prdCntry = ""
    for tag in tags_prdCntry:
        text_prdCntry += tag.text
    c23.append(text_prdCntry.lower())

    #'lang' column(c24)
    text_lang = ""
    for tag in tags_lang:
        text_lang += tag.text
    c24.append(text_lang.lower())

    # 'synop' column(c1)
    text_synop = ""
    for tag in tags_synop:
        text_synop += tag.text
    c1.append(text_synop.lower())

data += c2; data += c3; data += c4; data += c5; data += c6; data += c7; data += c8; data += c9; data += c10; data += c11; data += c12; data += c13; data += c14; data += c15; data += c16; data += c17; data += c18;
data += c19; data += c20; data += c21; data += c22; data += c23; data += c24; data += c1;

columns = ['dom_bo','int_bo','wrld_bo','dvd_sales','blu_sales','total_sales','opening','legs','share',
           'budget','theater_opening', 'theater_max','inf_dom_bo','vdo_release','mpaa','series','kwrds','src',
           'prd_mthd','creative_type','prd_company','prd_country','lang','synop']
df = pd.DataFrame([data], columns=columns)
df.to_csv('/home/pirl/A3_/proj_bigdata/hanbin/test.csv', header=True, index=False)

