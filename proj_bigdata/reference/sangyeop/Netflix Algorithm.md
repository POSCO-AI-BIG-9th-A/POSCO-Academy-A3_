## Netflix Algorithm(Day1)





[Netflix 공식사이트 추천 콘텐츠 시스템 작동방법](https://help.netflix.com/ko/node/100639?ba=SwiftypeResultClick&q=Netflix%EC%9D%98%20%EC%B6%94%EC%B2%9C%20%EC%BD%98%ED%85%90%EC%B8%A0%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EC%9E%91%EB%8F%99%20%EB%B0%A9%EB%B2%95)

[이전 분류모델 CINEMATCH](https://www.slideshare.net/itsociety/4-151106-58384116)

[kaggle netflix dataset](https://www.kaggle.com/netflix-inc/netflix-prize-data)

[넷플릭스 Tagger](https://biz.chosun.com/site/data/html_dir/2019/05/09/2019050901303.html)

[추천시스템 Trend](http://hoondongkim.blogspot.com/2019/03/recommendation-trend.html)

[Netflix Prize](http://www.shalomeir.com/2014/11/netflix-prize-1/)

[Model-based Collaborative Filtering algorithm](http://www.astronomer.rocks/news/articleView.html?idxno=86454)

[협업필터링 장단점](http://blog.skby.net/%ED%98%91%EC%97%85-%ED%95%84%ED%84%B0%EB%A7%81-collaborative-filtering/)

[넷플릭스 알고리즘 간단 설명](http://www.kocca.kr/insight/vol05/vol05_04.pdf)

[추천 시스템](https://lsjsj92.tistory.com/564)



현재 넷플릭스가 사용하는 알고리즘은 모델 기반 협업 필터링(Model-based Collaborative Filtering algorithm)





## Recommendation System 활용사례(Day2)

#### 아마존

전자상거래분야 추천시스템
Meta-data : 평점(Rating), 구매행위(Buying Behavior), 검색행위(BrowsingBehavior)
평점의 분류 : 직접 사용자가 매기는 명시적인 평점과 구매행위, 피드백을 가공한 암묵적인 평가

아마존 북매치 => 전체 매출의 35% 담당



## 잠재원인(Day2)

컨텐츠 자체 제작 능력 부족



자사/경쟁사 자체 제작 콘텐츠 건수 및 담당 인력 / 인사부서 협조요청

자사/경쟁사 콘텐츠 전략 및 투자 규모 / 영업 DB활용

자사/경쟁사 콘텐츠 특징 및 성과 / 영업 DB활용 

자사/경쟁사 콘텐츠 광고 노출건수, 국내외 커뮤니티 반응 / 인터넷 조사



## 데이터 수집계획(Day3)

추천시스템 연구동향 한번 보기

Data 목록

- moive_customer.csv(영화 정보)
- movie_download.csv(영화 Download 현황)
- moive_inventory.csv(Download 판권보유 영화 정보)
- moive_meta.csv(영화 정보)
- movie_price.csv(영화 download 책정 금액)

imdb => 장르가 알파벳 sort 되어있음.

[omdb](http://www.omdbapi.com/)

[영화추천시스템](https://www.kaggle.com/alsojmc/movie-recommender-systems)



## 데이터 항목의 의미와 유형 확인(Day4)

발표차례, 단체 PPT 부분 하기
content filtering 을 활용해보는건 어때?(정지성)



## 데이터 정제(Day4)

결측치 customer 파일 담당.ㅇ

|      | customer_id | gender | state |  age | age_group | married | kids_under12 | register_year | drop_flag | drop_year |
| ---- | ----------: | -----: | ----: | ---: | --------: | ------: | -----------: | ------------: | --------: | --------: |
| 결   |           X |      X |     X |    X |         X |       X |            X |             X |         X |         X |
| 이   |           X |      X |     X |    X |         X |       X |            X |             X |         X |         X |

회원정보에 없는데 download 한 경우도 없음. 
나이대와 나이정보도 틀린 것 없음.



교수님 : 예상치(Y)도 고려하면서 해보는게 좋다.

목표와 목적의 차이

- 목표는 보다 구체적이고 수치가 나와야함(target)
- 목적은 궁극적으로 도달할 방향.

#### 데이터 정제

- 다운로드 년도과 regi 년도 확인

