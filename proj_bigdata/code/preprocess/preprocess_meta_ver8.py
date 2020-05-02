import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

df_meta = pd.read_csv("../../data/cleaned/movie_meta_cleaned_ver7.csv", engine= "python", encoding='utf-8')

# 한빈
id_hb = ['tt1937264','tt2176228','tt0100142','tt0059592','tt1241226',
      'tt2290113','tt0188030','tt1781784','tt0063350','tt0093200',
      'tt3072636','tt3672742','tt0109445','tt1727770','tt0374563',
      'tt0475937','tt2141751','tt0997047','tt0467110','tt3442006',
      'tt0401815','tt1395025','tt2905838','tt4853102','tt1151359',
      'tt0796368','tt1502712','tt2837574','tt2273657','tt0145503',
      'tt0808331','tt1183374','tt1407084','tt0352994','tt0454776',
      'tt2944198','tt3577624','tt1853643','tt2674430','tt7026672',
      'tt2883512','tt1164999','tt2356180','tt4326444','tt5789976',
      'tt4005402','tt4437216','tt1321511','tt2397535','tt1951261',
      'tt2070776','tt1786751','tt5108476','tt6588966','tt6527426',
      'tt3405236'
      ]
opening_hb = [9,1,1,1,3,
           5,14,12,1,15,
           10,31,2,46,1061,
           488,2,2706,3013,482,
           14,122,271,1325,3,
           33,3995,5,831,4,
           6,9,231,45,791,
           1,2,3,11,1667,
           6,59,140,6,11,
           27,20,583,20,3555,
           3,1,284,73,295,
           265
           ]
total_hb = [9,1,5,2,3,
         5,72,12,8,15,
         10,31,84,46,1061,
         488,16,2706,3013,482,
         32,122,271,1325,6,
         193,4004,1042,856,153,
         152,9,231,45,1162,
         1,2,3,11,1669,
         1298,191,140,31,2,
         27,20,583,20,3565,
         58,100,284,73,300,
         265
         ]
L_hb = list(zip(id_hb,opening_hb,total_hb))
#진명
id_jm=['tt2584018','tt0094947','tt0076009','tt0076451','tt0077296','tt0112697','tt0049833','tt0093105','tt0071562','tt0104215',
'tt4878482','tt0070047','tt0066206','tt0054331','tt0061452','tt0079758','tt0082934','tt0053580','tt3453052','tt2968804','tt1034302','tt0059113','tt0101921','tt0072684',
'tt0108550','tt0102782','tt1592873','tt3658772','tt0062622','tt0108320','tt0056197','tt0063385','tt0076538','tt2113659','tt3202120','tt1320291','tt2300975','tt2556874','tt1725969','tt2396589','tt0213985','tt0062512','tt0057193','tt2077908','tt0067093','tt0059800','tt0097499','tt0062711','tt0043949',
'tt0059742','tt0079588','tt0079116','tt0064757','tt0107616','tt0105151','tt0102915','tt5153288','tt2112277','tt4060866','tt0097239','tt0263734','tt1602098','tt0242527','tt1772422','tt3488328','tt0066995','tt0107822','tt0070328','tt0071577','tt0071807','tt0085868','tt0076175','tt3401748'
         ]
opening_jm = [98,3,703,0,0,1653,0,4,0,501,20,0,0,0,0,0,0,0,1,9,10,0,5,1,6,1246,86,250,0,0,0,0,0,34,1,36,0,243,27,19,1,0,
              0,6,456,0,3,0,0,0,0,815,0,3,23,140,20,23,0,3,207,245,322,33,19,0,4,0,0,0,180,0,289]
total_jm = [98,762,703,0,0,1922,0,1598,0,501,20,0,0,0,0,0,0,0,10,9,13,0,1331,1,611,1246,86,250,0,0,0,0,0,34,1,36,0,243,
            27,19,1,0,0,7,456,0,134,0,0,0,0,815,0,204,452,140,223,23,0,1528,207,245,322,33,42,0,671,0,0,0,180,0,297]
L_jm = list(zip(id_jm,opening_jm,total_jm))
#다연
id_dy = ['tt0106677', 'tt1255953', 'tt0091763', 'tt0107750', 'tt0101412', 'tt0330602', 'tt3335606', 'tt0095271',
         'tt0083833', 'tt0098546', 'tt1529567', 'tt0110005', 'tt0102443', 'tt0102307', 'tt0117666', 'tt0095484',
         'tt0109831', 'tt0104036', 'tt0096219']
opening_dy = [183, 11, 1306, 668, 227, 99, 25, 1679, 21, 1295, 11, 2, 7, 3, 3, 90, 1064, 6, 6]
total_dy = [214, 90, 1564, 668, 227, 100, 25, 1679, 30, 1295, 12, 57, 7, 37, 1020, 107, 1069, 1097, 653]
L_dy = list(zip(id_dy,opening_dy,total_dy))
#채은
id_ce = ['tt0149624', 'tt2788710', 'tt0110074', 'tt0091757', 'tt1817771', 'tt1935194', 'tt0095016', 'tt0107818',
         'tt0093389', 'tt2039393', 'tt0107007', 'tt0114614', 'tt0101889', 'tt0064418', 'tt1833673', 'tt0108101',
         'tt0075860', 'tt0081353', 'tt0109348', 'tt3319920', 'tt0107719', 'tt0109707', 'tt1403241', 'tt0091934',
         'tt0083001', 'tt0097165', 'tt0079550', 'tt0107943', 'tt0352277', 'tt0097965', 'tt1487931']
opening_ce = [1483, 331, 5, 1108, 107, 20, 21, 4, 5, 2478, 124, 1341, 10, 669, 239, 3, 272, 901, 2, 100, 786, 2, 12,
              401, 1, 8, 575, 94, 16, 12, 2]
total_ce = [1483, 581, 126, 1108, 107, 20, 1713, 1604, 817, 2494, 239, 1363, 1546, 669, 239, 1023, 571, 901, 278, 100,
            786, 623, 12, 401, 19, 1109, 575, 517, 410, 514, 2]
L_ce = list(zip(id_ce,opening_ce,total_ce))
#상엽
id_sy = ['tt0029852','tt0338497','tt1754633','tt1703199','tt2494362','tt0363095','tt2126362','tt0066808','tt0040525',
         'tt2980794','tt0060438','tt3499458','tt0075314','tt2268573','tt0074285','tt0057012','tt0044081','tt0061747',
         'tt0822858','tt1653002','tt0071360','tt0064990','tt0092675','tt0031679','tt0038109','tt0109759','tt0027977',
         'tt3504048','tt8043306','tt0473107','tt2017486','tt0029583','tt0028216','tt2282016','tt0032976','tt0046126',
         'tt0098724','tt0044079','tt0048750','tt0043456','tt0105236','tt0051207','tt0806147','tt0065579','tt0080749',
         'tt0067756','tt0075148','tt0057590','tt0082533','tt0065466','tt0049452','tt0401462','tt2852376','tt4733536',
         'tt0323120','tt5022702','tt8361028','tt2141739','tt0047296','tt1769363','tt0034492','tt0066832','tt0069704',
         'tt0308411','tt0110057','tt2016335','tt0024216','tt0027125','tt0066580','tt0076257','tt0058182','tt0071206',
         'tt2246526']
opening_sy = [0, 4, 1, 0, 0, 1, 0, 0, 0, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 123, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 4, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 3, 0, 0, 0,
              781, 0, 2, 0, 1]
total_sy = [0, 7, 2, 0, 0, 1, 0, 0, 0, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 124, 0, 0, 433, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 534, 0, 0, 0, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 18, 262, 0, 0, 0,
            781, 0, 63, 0, 1]
L_sy = list(zip(id_sy,opening_sy,total_sy))
#경원
id_kw =['tt0031381','tt0060665','tt0016641','tt0059418','tt0072251','tt0042200','tt3205376','tt0065446','tt0064665','tt0080339',
        'tt0061809','tt0068611','tt0060490','tt0088993','tt2166834','tt2761578','tt0049055','tt0083739','tt0056217','tt0038650',
        'tt0077975','tt0058150','tt0050212','tt0077362','tt0073312','tt0053604','tt0051459','tt0065462','tt0074512','tt0061107',
        'tt0053793','tt0067992','tt0116361','tt1841642','tt2398249','tt1922679','tt0482461','tt0062138','tt0038589','tt0042332',
        'tt0053291','tt0072431','tt0032138','tt0078872','tt0071230','tt0093512','tt0857295','tt0045152','tt0102494','tt1666335',
        'tt3300572','tt3333870','tt6952960','tt1995477','tt0044030','tt0098503','tt0092695','tt0032910','tt0032455','tt0067116',
        'tt0449000','tt0036868','tt1038988','tt2215673','tt0038787','tt0061811','tt0070707','tt0068555','tt0056592','tt0056193',
        'tt0032273','tt0039416','tt0090327']
opening_kw = [0, 0, 0, 1, 0, 0, 50, 0, 0, 0, 0, 0, 0, 168, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 6, 72, 0, 49, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 1, 0, 0, 3, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 19, 0, 0, 0, 0, 0, 0, 1, 0, 0, 15]
total_kw = [0, 0, 0, 3, 0, 0, 54, 0, 0, 0, 0, 0, 0, 168, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 6, 76, 0, 49, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 3, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 20, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1068]
L_kw = list(zip(id_kw,opening_kw,total_kw))

L = L_hb + L_jm + L_dy + L_ce + L_sy + L_kw
for i in L:
    df_meta.loc[df_meta['movie_id'] == i[0], 'theater_opening'] = i[1]
    df_meta.loc[df_meta['movie_id'] == i[0], 'theater_total'] = i[2]

for i in df_meta[df_meta['theater_opening'].isna()].index:
    df_meta.loc[i,'theater_opening'] = 0
for i in df_meta[df_meta['theater_total'].isna()].index:
    df_meta.loc[i,'theater_total'] = 0

df_meta.to_csv('../../data/cleaned/movie_meta_cleaned_ver8.csv', header=True, index=False)









