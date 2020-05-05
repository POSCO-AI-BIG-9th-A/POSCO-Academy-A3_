import pandas as pd
# dvd_sales, blu_sales 추가!
# 꼼꼼히 하겠습니다 죄송해용 by koyo
def InsertSale(df_raw):
    for i in df_raw.index:
        movie_id = df_raw.loc[i,"movie_id"]
        if movie_id == "tt0083001":
            # Roar(1981)
            df_raw.loc[i,"dvd_sales"] = "."
            df_raw.loc[i,"blu_sales"] = "676644"
            df_raw.loc[i,"total_sales"] = "676644"
        if movie_id == "tt0407304":
            # War of the Worlds (2005)
            df_raw.loc[i,"dvd_sales"] = "."
            df_raw.loc[i,"blu_sales"] = "95409"
            df_raw.loc[i,"total_sales"] = "95409"
        if movie_id == "tt0120737":
            # The Lord of the Rings: The Fellowship of the Ring (2001)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "4214981"
            df_raw.loc[i, "total_sales"] = "4214981"
        if movie_id == "tt0181689":
            # Minority Report
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "164308"
            df_raw.loc[i, "total_sales"] = "164308"
        if movie_id == "tt0133240":
            # Treasure Planet (2002)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "263364"
            df_raw.loc[i, "total_sales"] = "263364"
        if movie_id == "tt0217505":
            # Gangs of New York (2002)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "124636"
            df_raw.loc[i, "total_sales"] = "124636"
        if movie_id == "tt0119116":
            # The Fifth Element (1997)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "9311346"
            df_raw.loc[i, "total_sales"] = "9311346"
        if movie_id == "tt0167261":
            # The Lord of the Rings: The Two Towers (2002)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "4774313"
            df_raw.loc[i, "total_sales"] = "4774313"
        if movie_id == "tt0113492":
            # Judge Dredd (1995)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "121773"
            df_raw.loc[i, "total_sales"] = "121773"
        if movie_id == "tt0244244":
            # Swordfish (2001)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "200916"
            df_raw.loc[i, "total_sales"] = "200916"
        if movie_id == "tt0146309":
            # Thirteen Days (2000)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "202150"
            df_raw.loc[i, "total_sales"] = "202150"
        if movie_id == "tt0112573":
            # Thirteen Days (2000)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "7328028"
            df_raw.loc[i, "total_sales"] = "7328028"
        if movie_id == "tt0096438":
            #Who Framed Roger Rabbit (1988)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1198646"
            df_raw.loc[i, "total_sales"] = "1198646"
        if movie_id == "tt0120815":
            # Saving Private Ryan (1998)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "9403638"
            df_raw.loc[i, "total_sales"] = "9403638"
        if movie_id == "tt0112384":
            # Apollo 13 (1995)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "469423"
            df_raw.loc[i, "total_sales"] = "469423"
        if movie_id == "tt0133093":
            # The Matrix (1999)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "4050617"
            df_raw.loc[i, "total_sales"] = "4050617"
        if movie_id == "tt1951181":
            # The Immigrant (2013)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "19401"
            df_raw.loc[i, "total_sales"] = "19401"
        if movie_id == "tt0089469":
            # Legend (1986)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "152914"
            df_raw.loc[i, "total_sales"] = "152914"
        if movie_id == "tt0395495":
            # Catch and Release (2007)
            df_raw.loc[i, "dvd_sales"] = "12504124"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "12504124"
        if movie_id == "tt0865554":
            # I Know Who Killed Me (2007)
            df_raw.loc[i, "dvd_sales"] = "27849387"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "27849387"
        if movie_id == "tt0375679":
            # Crash (2004)
            df_raw.loc[i, "dvd_sales"] = "25528438"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "25528438"
        if movie_id == "tt0455326":
            # Crash (2004)
            df_raw.loc[i, "dvd_sales"] = "12249683"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "12249683"
        if movie_id == "tt0780595":
            # Redline (2007)
            df_raw.loc[i, "dvd_sales"] = "5487604"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "5487604"
        if movie_id == "tt0356910":
            # Mr. and Mrs. Smith (2005)
            df_raw.loc[i, "dvd_sales"] = "16436865"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "16436865"
        if movie_id == "tt0121766":
            # Star Wars Ep. III: Revenge of the Sith (2005)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "234330"
            df_raw.loc[i, "total_sales"] = "234330"
        if movie_id == "tt0063350":
            # Night of the Living Dead (1968)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "672620"
            df_raw.loc[i, "total_sales"] = "672620"
        if movie_id == "tt0034587":
            # Cat People (1942)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "730008"
            df_raw.loc[i, "total_sales"] = "730008"
        if movie_id == "tt1211890":
            # Middle of Nowhere (2012)
            df_raw.loc[i, "dvd_sales"] = "155607"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "155607"
        if movie_id == "tt0015624":
            # The Big Parade (1925)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "268474"
            df_raw.loc[i, "total_sales"] = "268474"
        if movie_id == "tt1241226":
            # Locker 13 (2014)
            df_raw.loc[i, "dvd_sales"] = "13468"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "13468"
        if movie_id == "tt0468526":
            # Old Joy (2006)
            df_raw.loc[i, "dvd_sales"] = "15517"
            df_raw.loc[i, "blu_sales"] = "18986"
            df_raw.loc[i, "total_sales"] = "34503"
        if movie_id == "tt0077651":
            # Halloween (1978)
            df_raw.loc[i, "dvd_sales"] = "6873507"
            df_raw.loc[i, "blu_sales"] = "1531093"
            df_raw.loc[i, "total_sales"] = "8404600"
        if movie_id == "tt0071853":
            # Monty Python and the Holy Grail (1975)
            df_raw.loc[i, "dvd_sales"] = "27370829"
            df_raw.loc[i, "blu_sales"] = "22054133"
            df_raw.loc[i, "total_sales"] = "49424962"
        if movie_id == "tt0374900":
            # Napoleon Dynamite (2004)
            df_raw.loc[i, "dvd_sales"] = "36163312"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "36163312"
        if movie_id == "tt2246526":
            # Born to Fly: Elizabeth Streb vs. Gravity (2014)
            df_raw.loc[i, "dvd_sales"] = "31215"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "31215"
        if movie_id == "tt0058182":
            # A Hard Day's Night (1964)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1151142"
            df_raw.loc[i, "total_sales"] = "1151142"
        if movie_id == "tt0066580":
            # Woodstock (1970)
            df_raw.loc[i, "dvd_sales"] = "22609935"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "22609935"
        if movie_id == "tt0110057":
            # Hoop Dreams (1994)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "155265"
            df_raw.loc[i, "total_sales"] = "155265"
        if movie_id == "tt3569356":
            # Not Cool (2014)
            df_raw.loc[i, "dvd_sales"] = "114671"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "114671"
        if movie_id == "tt0034492":
            #Bambi (1942)
            df_raw.loc[i, "dvd_sales"] = "63879327"
            df_raw.loc[i, "blu_sales"] = "33295406"
            df_raw.loc[i, "total_sales"] = "97174733"
        if movie_id == "tt2884206":
            # I Origins (2014)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "410507"
            df_raw.loc[i, "total_sales"] = "410507"
        if movie_id == "tt0057590":
            # Tom Jones (1963)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "189223"
            df_raw.loc[i, "total_sales"] = "189223"
        if movie_id == "tt0075148":
            # Rocky (1976)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "893524"
            df_raw.loc[i, "total_sales"] = "893524"
        if movie_id == "tt2723576":
            # The Sleepwalker (2014)
            df_raw.loc[i, "dvd_sales"] = "23188"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "23188"
        if movie_id == "tt0073629":
            # The Rocky Horror Picture Show
            df_raw.loc[i, "dvd_sales"] = "8803296"
            df_raw.loc[i, "blu_sales"] = "778738"
            df_raw.loc[i, "total_sales"] = "9582034"
        if movie_id == "tt0105236":
            # Reservoir Dogs (1992)
            df_raw.loc[i, "dvd_sales"] = "5050638"
            df_raw.loc[i, "blu_sales"] = "146089"
            df_raw.loc[i, "total_sales"] = "5196727"
        if movie_id == "tt0387564":
            # Saw (2004)
            df_raw.loc[i, "dvd_sales"] = "11955387"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "11955387"
        if movie_id == "tt0029583":
            # Snow White and the Seven Dwarfs (1937)
            df_raw.loc[i, "dvd_sales"] = "86022564"
            df_raw.loc[i, "blu_sales"] = "97301562"
            df_raw.loc[i, "total_sales"] = "183324126"
        if movie_id == "tt0118789":
            # Buffalo '66 (1998)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "229673"
            df_raw.loc[i, "total_sales"] = "229673"
        if movie_id == "tt0075314":
            # Taxi Driver (1976)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "354025"
            df_raw.loc[i, "total_sales"] = "354025"
        if movie_id == "tt1462758":
            # Buried (2010)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1357092"
            df_raw.loc[i, "total_sales"] = "1357092"
        if movie_id == "tt0056592":
            #To Kill a Mockingbird (1962)
            df_raw.loc[i, "dvd_sales"] = "4907000"
            df_raw.loc[i, "blu_sales"] = "2374694"
            df_raw.loc[i, "total_sales"] = "7281694"
        if movie_id == "tt0061811":
            #In the Heat of the Night (1967)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "549510"
            df_raw.loc[i, "total_sales"] = "549510"
        if movie_id == "tt0038787":
            # Notorious (1946)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "985082"
            df_raw.loc[i, "total_sales"] = "985082"
        if movie_id == "tt0032910":
            # Pinocchio (1940)
            df_raw.loc[i, "dvd_sales"] = "78578335"
            df_raw.loc[i, "blu_sales"] = "13990282"
            df_raw.loc[i, "total_sales"] = "92568617"
        if movie_id == "tt0333766":
            # Garden State (2004)
            df_raw.loc[i, "dvd_sales"] = "13975161"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "13975161"
        if movie_id == "tt2247692":
            # 2016: Obama's America (2012)
            df_raw.loc[i, "dvd_sales"] = "7180892"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "7180892"
        if movie_id == "tt0093512":
            # Maurice (1987)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "139847"
            df_raw.loc[i, "total_sales"] = "139847"
        if movie_id == "tt0071230":
            # Blazing Saddles (1974)
            df_raw.loc[i, "dvd_sales"] = "11245290"
            df_raw.loc[i, "blu_sales"] = "136494"
            df_raw.loc[i, "total_sales"] = "11381784"
        if movie_id == "tt0078872":
            #The Black Stallion (1979)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1730141"
            df_raw.loc[i, "total_sales"] = "1730141"
        if movie_id == "tt0032138":
            # The Wizard of Oz (1939)
            df_raw.loc[i, "dvd_sales"] = "95578243"
            df_raw.loc[i, "blu_sales"] = "32159903"
            df_raw.loc[i, "total_sales"] = "127738146"
        if movie_id == "tt0072431":
            # Young Frankenstein (1974)
            df_raw.loc[i, "dvd_sales"] = "17517371"
            df_raw.loc[i, "blu_sales"] = "51344"
            df_raw.loc[i, "total_sales"] = "17568715"
        if movie_id == "tt0042332":
            # Cinderella (1950)
            df_raw.loc[i, "dvd_sales"] = "63937464"
            df_raw.loc[i, "blu_sales"] = "42851254"
            df_raw.loc[i, "total_sales"] = "106788718"
        if movie_id == "tt0067992":
            # Willy Wonka & the Chocolate Factory (1971)
            df_raw.loc[i, "dvd_sales"] = "13326488"
            df_raw.loc[i, "blu_sales"] = "224516"
            df_raw.loc[i, "total_sales"] = "13551004"
        if movie_id == "tt0053793":
            # Elmer Gantry (1960)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "193677"
            df_raw.loc[i, "total_sales"] = "193677"
        if movie_id == "tt0118570":
            # Air Bud (1997)
            df_raw.loc[i, "dvd_sales"] = "1222580"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "1222580"
        if movie_id == "tt0236388":
            # The Bridge on the River Kwai (1957)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "228881"
            df_raw.loc[i, "total_sales"] = "228881"
        if movie_id == "tt0077975":
            # National Lampoon's Animal House (1978)
            df_raw.loc[i, "dvd_sales"] = "1094005"
            df_raw.loc[i, "blu_sales"] = "378294"
            df_raw.loc[i, "total_sales"] = "1472299"
        if movie_id == "tt0038650":
            # It’s a Wonderful Life (1946)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "3627620"
            df_raw.loc[i, "total_sales"] = "3627620"
        if movie_id == "tt0083739":
            # Class of 1984 (1982)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "121900"
            df_raw.loc[i, "total_sales"] = "121900"
        if movie_id == "tt0085334":
            # Class of 1984 (1982)
            df_raw.loc[i, "dvd_sales"] = "65680448"
            df_raw.loc[i, "blu_sales"] = "5359140"
            df_raw.loc[i, "total_sales"] = "71039588"
        if movie_id == "tt0088993":
            # Day of the Dead (1985)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "335973"
            df_raw.loc[i, "total_sales"] = "335973"
        if movie_id == "tt0031381":
            # Gone with the Wind (1939)
            df_raw.loc[i, "dvd_sales"] = "59080803"
            df_raw.loc[i, "blu_sales"] = "42870906"
            df_raw.loc[i, "total_sales"] = "101951709"
        if movie_id == "tt0454987":
            #Let's Go to Prison (2006)
            df_raw.loc[i, "dvd_sales"] = "4941065"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "4941065"
        if movie_id == "tt0057115":
            #The Great Escape (1963)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "785218"
            df_raw.loc[i, "total_sales"] = "785218"
        if movie_id == "tt0046183":
            #Peter Pan (1953)
            df_raw.loc[i, "dvd_sales"] = "67703398"
            df_raw.loc[i, "blu_sales"] = "26604141"
            df_raw.loc[i, "total_sales"] = "94307539"
        if movie_id == "tt0115736":
            #Bound (1996)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "237931"
            df_raw.loc[i, "total_sales"] = "237931"
        if movie_id == "tt0083929":
            # Fast Times at Ridgemont High (1982)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "278764"
            df_raw.loc[i, "total_sales"] = "278764"
        if movie_id == "tt0098546":
            # UHF (1989)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1216029"
            df_raw.loc[i, "total_sales"] = "1216029"
        if movie_id == "tt0259446":
            # My Big Fat Greek Wedding (2002)
            df_raw.loc[i, "dvd_sales"] = "12024200"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "12024200"
        if movie_id == "tt0473024":
            # Crossover (2006)
            df_raw.loc[i, "dvd_sales"] = "6118812"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "6118812"
        if movie_id == "tt7339792":
            # Unbroken: Path to Redemption (2018)
            df_raw.loc[i, "dvd_sales"] = "762459"
            df_raw.loc[i, "blu_sales"] = "1915724"
            df_raw.loc[i, "total_sales"] = "2678183"
        if movie_id == "tt0038499":
            # Duel in the Sun (1946)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "79250"
            df_raw.loc[i, "total_sales"] = "79250"
        if movie_id == "tt0055614":
            #West Side Story (1961)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "3552841"
            df_raw.loc[i, "total_sales"] = "3552841"
        if movie_id == "tt0058331":
            # Mary Poppins (1964)
            df_raw.loc[i, "dvd_sales"] = "191197283"
            df_raw.loc[i, "blu_sales"] = "7037731"
            df_raw.loc[i, "total_sales"] = "198235014"
        if movie_id == "tt0091763":
            # Platoon (1986)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "162564"
            df_raw.loc[i, "total_sales"] = "162564"
        if movie_id == "tt0077631":
            # Grease (1978)
            df_raw.loc[i, "dvd_sales"] = "23420295"
            df_raw.loc[i, "blu_sales"] = "230742"
            df_raw.loc[i, "total_sales"] = "23651037"
        if movie_id == "tt0088247":
            # The Terminator (1984)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "636919"
            df_raw.loc[i, "total_sales"] = "636919"
        if movie_id == "tt0790712":
            # The Messenger (2009)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "487218"
            df_raw.loc[i, "total_sales"] = "487218"
        if movie_id == "tt1723811":
            # Shame (2011)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1408234"
            df_raw.loc[i, "total_sales"] = "1408234"
        if movie_id == "tt0066769":
            # The Andromeda Strain (1971)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "259255"
            df_raw.loc[i, "total_sales"] = "259255"
        if movie_id == "tt4131800":
            # My Little Pony: The Movie (2017)
            df_raw.loc[i, "dvd_sales"] = "4884601"
            df_raw.loc[i, "blu_sales"] = "3776460"
            df_raw.loc[i, "total_sales"] = "8661061"
        if movie_id == "tt0080661":
            # Dressed to Kill (1980)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "803066"
            df_raw.loc[i, "total_sales"] = "803066"
        if movie_id == "tt0106677":
            # Dazed and Confused (1993)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "237624"
            df_raw.loc[i, "total_sales"] = "237624"
        if movie_id == "tt0085868":
            # Losin' It (1983)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "10044"
            df_raw.loc[i, "total_sales"] = "10044"
        if movie_id == "tt0103893":
            # Losin' It (1983)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "185760"
            df_raw.loc[i, "total_sales"] = "185760"
        if movie_id == "tt0395584":
            # The Devil's Rejects (2005)
            df_raw.loc[i, "dvd_sales"] = "3980723"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "3980723"
        if movie_id == "tt0071577":
            # The Great Gatsby (1974)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "4935183"
            df_raw.loc[i, "total_sales"] = "4935183"
        if movie_id == "tt0068646":
            # The Godfather (1972)
            df_raw.loc[i, "dvd_sales"] = "1228410"
            df_raw.loc[i, "blu_sales"] = "250602"
            df_raw.loc[i, "total_sales"] = "1479012"
        if movie_id == "tt1778304":
            # Paranormal Activity 3 (2011)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "3567561"
            df_raw.loc[i, "total_sales"] = "3567561"
        if movie_id == "tt1001562":
            # Witless Protection (2008)
            df_raw.loc[i, "dvd_sales"] = "18828847"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "18828847"
        if movie_id == "tt0086582":
            # The Wicked Lady (1983)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "63204"
            df_raw.loc[i, "total_sales"] = "63204"
        if movie_id == "tt0102915":
            # Showdown in Little Tokyo (1991)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "60387"
            df_raw.loc[i, "total_sales"] = "60387"
        if movie_id == "tt0104454":
            # Howards End (1992)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "177240"
            df_raw.loc[i, "total_sales"] = "177240"
        if movie_id == "tt0079116":
            # Escape from Alcatraz (1979)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "74480"
            df_raw.loc[i, "total_sales"] = "74480"
        if movie_id == "tt0092005":
            #Stand by Me (1986)
            df_raw.loc[i, "dvd_sales"] = "656113"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "656113"
        if movie_id == "tt0079588":
            # The Muppet Movie (1979)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1108022"
            df_raw.loc[i, "total_sales"] = "1108022"
        if movie_id == "tt0087277":
            # Pulp Fiction (1994)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "5745290"
            df_raw.loc[i, "total_sales"] = "5745290"
        if movie_id == "tt0059742":
            # The Sound of Music (1965)
            df_raw.loc[i, "dvd_sales"] = "13193467"
            df_raw.loc[i, "blu_sales"] = "62659611"
            df_raw.loc[i, "total_sales"] = "75853078"
        if movie_id == "tt0126886":
            # Election (1999)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "69778"
            df_raw.loc[i, "total_sales"] = "69778"
        if movie_id == "tt0079826":
            #The Rose (1979)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "205050"
            df_raw.loc[i, "total_sales"] = "205050"
        if movie_id == "tt0093437":
            #The Lost Boys (1987)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "791882"
            df_raw.loc[i, "total_sales"] = "791882"
        if movie_id == "tt0454082":
            #Black Christmas (2006)
            df_raw.loc[i, "dvd_sales"] = "29455713"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "29455713"
        if movie_id == "tt0366551":
            #Harold & Kumar Go to White Castle (2004)
            df_raw.loc[i, "dvd_sales"] = "30609751"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "30609751"
        if movie_id == "tt0324216":
            #The Texas Chainsaw Massacre (2003)
            df_raw.loc[i, "dvd_sales"] = "2975100"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "2975100"
        if movie_id == "tt0057193":
            #It's a Mad Mad Mad Mad World (1963)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1492246"
            df_raw.loc[i, "total_sales"] = "1492246"
        if movie_id == "tt1777595":
            #50 to 1 (2014)
            df_raw.loc[i, "dvd_sales"] = "615278"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "615278"
        if movie_id == "tt0151804":
            #Office Space (1999)
            df_raw.loc[i, "dvd_sales"] = "7960168"
            df_raw.loc[i, "blu_sales"] = "167164"
            df_raw.loc[i, "total_sales"] = "8127332"
        if movie_id == "tt0089348":
            # Invasion U.S.A (1985)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "57530"
            df_raw.loc[i, "total_sales"] = "57530"
        if movie_id == "tt0846308":
            # Kit Kittredge: An American Girl (2008)
            df_raw.loc[i, "dvd_sales"] = "17979198"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "17979198"
        if movie_id == "tt0208092":
            # Snatch (2000)
            df_raw.loc[i, "dvd_sales"] = "828130"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "828130"
        if movie_id == "tt0089461":
            # The Last Dragon (1985)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "303225"
            df_raw.loc[i, "total_sales"] = "303225"
        if movie_id == "tt0076538":
            # Pete’s Dragon (1977)
            df_raw.loc[i, "dvd_sales"] = "16642434"
            df_raw.loc[i, "blu_sales"] = "558595"
            df_raw.loc[i, "total_sales"] = "17201029"
        if movie_id == "tt0204946":
            # Bring it On (2000)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "311139"
            df_raw.loc[i, "total_sales"] = "311139"
        if movie_id == "tt0119217":
            # Good Will Hunting (1997)
            df_raw.loc[i, "dvd_sales"] = "485060"
            df_raw.loc[i, "blu_sales"] = "4866299"
            df_raw.loc[i, "total_sales"] = "5351359"
        if movie_id == "tt0062622":
            # 2001: A Space Odyssey (1968)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "3069743"
            df_raw.loc[i, "total_sales"] = "3069743"
        if movie_id == "tt0083866":
            # ET: The Extra-Terrestrial (1982)
            df_raw.loc[i, "dvd_sales"] = "22176329"
            df_raw.loc[i, "blu_sales"] = "8682172"
            df_raw.loc[i, "total_sales"] = "30858501"
        if movie_id == "tt0078748":
            # Alien (1979)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "3433083"
            df_raw.loc[i, "total_sales"] = "3433083"
        if movie_id == "tt0101921":
            # Fried Green Tomatoes (1991)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "631488"
            df_raw.loc[i, "total_sales"] = "631488"
        if movie_id == "tt0059113":
            #Doctor Zhivago (1965)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "387992"
            df_raw.loc[i, "total_sales"] = "387992"
        if movie_id == "tt0087363":
            #Gremlins (1984)
            df_raw.loc[i, "dvd_sales"] = "14994711"
            df_raw.loc[i, "blu_sales"] = "152011"
            df_raw.loc[i, "total_sales"] = "15146722"
        if movie_id == "tt0098084":
            #Pet Sematary (1989)
            df_raw.loc[i, "dvd_sales"] = "595254"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "595254"
        if movie_id == "tt1416801":
            #Kill the Irishman (2011)
            df_raw.loc[i, "dvd_sales"] = "2911365"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "2911365"
        if movie_id == "tt0091276":
            #Invaders from Mars (1986)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "55273"
            df_raw.loc[i, "total_sales"] = "55273"
        if movie_id == "tt0104940":
            #The Muppet Christmas Carol (1992)
            df_raw.loc[i, "dvd_sales"] = "12953600"
            df_raw.loc[i, "blu_sales"] = "218448"
            df_raw.loc[i, "total_sales"] = "13172048"
        if movie_id == "tt0054331":
            #Spartacus (1960)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "143244"
            df_raw.loc[i, "total_sales"] = "143244"
        if movie_id == "tt0081633":
            #Time Bandits (1981)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1012280"
            df_raw.loc[i, "total_sales"] = "1012280"
        if movie_id == "tt0119396":
            #Jackie Brown (1997)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "176954"
            df_raw.loc[i, "total_sales"] = "176954"
        if movie_id == "tt0090329":
            #Witness (1985)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "197027"
            df_raw.loc[i, "total_sales"] = "197027"
        if movie_id == "tt0084726":
            #Star Trek II: The Wrath of Khan (1982)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "245580"
            df_raw.loc[i, "total_sales"] = "245580"
        if movie_id == "tt0070047":
            #The Exorcist (1973)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "950462"
            df_raw.loc[i, "total_sales"] = "950462"
        if movie_id == "tt0095489":
            #The Land Before Time (1988)
            df_raw.loc[i, "dvd_sales"] = "11723951"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "11723951"
        if movie_id == "tt0083722":
            #Cat People (1982)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "449390"
            df_raw.loc[i, "total_sales"] = "449390"
        if movie_id == "tt0093870":
            #RoboCop (1987)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "414346"
            df_raw.loc[i, "total_sales"] = "414346"
        if movie_id == "tt0049833":
            #The Ten Commandments (1956)
            df_raw.loc[i, "dvd_sales"] = "372607"
            df_raw.loc[i, "blu_sales"] = "1714689"
            df_raw.loc[i, "total_sales"] = "2087296"
        if movie_id == "tt0100758":
            #Teenage Mutant Ninja Turtles (1990)
            df_raw.loc[i, "dvd_sales"] = "949077"
            df_raw.loc[i, "blu_sales"] = "54619"
            df_raw.loc[i, "total_sales"] = "1003696"
        if movie_id == "tt0166924":
            #Mulholland Drive (2001)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "389084"
            df_raw.loc[i, "total_sales"] = "389084"
        if movie_id == "tt0310910":
            #Idlewild (2006)
            df_raw.loc[i, "dvd_sales"] = "9203028"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "9203028"
        if movie_id == "tt0118715":
            #The Big Lebowski (1998)
            df_raw.loc[i, "dvd_sales"] = "23056964"
            df_raw.loc[i, "blu_sales"] = "5896234"
            df_raw.loc[i, "total_sales"] = "28953198"
        if movie_id == "tt0093779":
            #The Princess Bride (1987)
            df_raw.loc[i, "dvd_sales"] = "53424348"
            df_raw.loc[i, "blu_sales"] = "2988720"
            df_raw.loc[i, "total_sales"] = "56413068"
        if movie_id == "tt0317132":
            #Because of Winn-Dixie (2005)
            df_raw.loc[i, "dvd_sales"] = "11613549"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "11613549"
        if movie_id == "tt0056172":
            # Lawrence of Arabia (1962)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "11792890"
            df_raw.loc[i, "total_sales"] = "11792890"
        if movie_id == "tt0094721":
            # Beetlejuice (1988)
            df_raw.loc[i, "dvd_sales"] = "12829122"
            df_raw.loc[i, "blu_sales"] = "381874"
            df_raw.loc[i, "total_sales"] = "13210996"
        if movie_id == "tt0117571":
            #Scream (1996)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "299511"
            df_raw.loc[i, "total_sales"] = "299511"
        if movie_id == "tt0169547":
            #American Beauty (1999)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "78983"
            df_raw.loc[i, "total_sales"] = "78983"
        if movie_id == "tt0092099":
            #Top Gun (1986)
            df_raw.loc[i, "dvd_sales"] = "16146163"
            df_raw.loc[i, "blu_sales"] = "3124834"
            df_raw.loc[i, "total_sales"] = "19270997"
        if movie_id == "tt0099785":
            #Home Alone (1990)
            df_raw.loc[i, "dvd_sales"] = "69591323"
            df_raw.loc[i, "blu_sales"] = "8235190"
            df_raw.loc[i, "total_sales"] = "77826513"
        if movie_id == "tt0079550":
            #Meteor (1979)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "134963"
            df_raw.loc[i, "total_sales"] = "134963"
        if movie_id == "tt0110413":
            #Léon (1994)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "1515800"
            df_raw.loc[i, "total_sales"] = "1515800"
        if movie_id == "tt0245686":
            #Joe Dirt (2001)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "205761"
            df_raw.loc[i, "total_sales"] = "205761"
        if movie_id == "tt0250720":
            #The Killing Fields (1984)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "490789"
            df_raw.loc[i, "total_sales"] = "490789"
        if movie_id == "tt0114388":
            #Sense and Sensibility (1995)
            df_raw.loc[i, "dvd_sales"] = "8637195"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "8637195"
        if movie_id == "tt0094291":
            #Wall Street (1987)
            df_raw.loc[i, "dvd_sales"] = "931435"
            df_raw.loc[i, "blu_sales"] = "191767"
            df_raw.loc[i, "total_sales"] = "1123202"
        if movie_id == "tt0159421":
            #The Adventures of Elmo in Grouchland (1999)
            df_raw.loc[i, "dvd_sales"] = "5891042"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "5891042"
        if movie_id == "tt0462395":
            #Larry the Cable Guy: Health Inspector (2006)
            df_raw.loc[i, "dvd_sales"] = "13266667"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "13266667"
        if movie_id == "tt0466856":
            #ATL (2006)
            df_raw.loc[i, "dvd_sales"] = "29907796"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "29907796"
        if movie_id == "tt0084827":
            #Tron (1982)
            df_raw.loc[i, "dvd_sales"] = "2126944"
            df_raw.loc[i, "blu_sales"] = "3141147"
            df_raw.loc[i, "total_sales"] = "5268091"
        if movie_id == "tt0090605":
            #Aliens (1986)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "10947988"
            df_raw.loc[i, "total_sales"] = "10947988"
        if movie_id == "tt0230600":
            #The Others (2001)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "229766"
            df_raw.loc[i, "total_sales"] = "229766"
        if movie_id == "tt1142800":
            # Madea Goes To Jail (2009)
            df_raw.loc[i, "dvd_sales"] = "30575808"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "30575808"
        if movie_id == "tt0118040":
            # Unforgettable (1996)
            df_raw.loc[i, "dvd_sales"] = "981236"
            df_raw.loc[i, "blu_sales"] = "388399"
            df_raw.loc[i, "total_sales"] = "1369635"
        if movie_id == "tt0088763":
            # Back to the Future (1985)
            df_raw.loc[i, "dvd_sales"] = "5514726"
            df_raw.loc[i, "blu_sales"] = "."
            df_raw.loc[i, "total_sales"] = "5514726"
        if movie_id == "tt0099348":
            # Dances with Wolves (1990)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "440239"
            df_raw.loc[i, "total_sales"] = "440239"
        if movie_id == "tt0081505":
            # The Shining(1980)
            df_raw.loc[i, "dvd_sales"] = "9604529"
            df_raw.loc[i, "blu_sales"] = "525765"
            df_raw.loc[i, "total_sales"] = "10130294"
        if movie_id == "tt0093773":
            # Predator(1987)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "3138174"
            df_raw.loc[i, "total_sales"] = "3138174"
        if movie_id == "tt1478839":
            # The Art of Racing in the Rain(2019)
            df_raw.loc[i, "dvd_sales"] = "3495682"
            df_raw.loc[i, "blu_sales"] = "2053535"
            df_raw.loc[i, "total_sales"] = "5549217"
        if movie_id == "tt0082648":
            # The Legend of the Lone Ranger (1981)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "91919"
            df_raw.loc[i, "total_sales"] = "91919"
        if movie_id == "tt0109707":
            # Ed Wood (1994)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "90464"
            df_raw.loc[i, "total_sales"] = "90464"
        if movie_id == "tt0090568":
            # 8 Million Ways to Die (1986)
            df_raw.loc[i, "dvd_sales"] = "."
            df_raw.loc[i, "blu_sales"] = "69159"
            df_raw.loc[i, "total_sales"] = "69159"




if __name__ == "__main__":
    df = pd.read_csv("../../data/cleaned/movie_meta_cleaned_final3.csv", engine="python", encoding="utf-8")
    print("dvd_sales, blu_sales 수정 전 :")
    print(df.loc[df["dvd_sales"]==".", "movie_id"].value_counts().size, df.loc[df["blu_sales"]==".", "movie_id"].value_counts().size)
    InsertSale(df)
    print("dvd_sales 수정 후 : ")
    print(df.loc[df["dvd_sales"]==".", "movie_id"].value_counts().size, df.loc[df["blu_sales"]==".", "movie_id"].value_counts().size)
    # print(df.duplicated(["movie_id"]).value_counts())
    df.to_csv("../../data/cleaned/movie_meta_cleaned_final4.csv", header=True, index=False)

