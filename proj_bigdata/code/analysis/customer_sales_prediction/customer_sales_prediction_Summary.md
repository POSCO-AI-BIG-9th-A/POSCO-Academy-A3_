## 고객별 연간 매출 예측

#### 대상 데이터

------

- movie_customer.csv
- 목표 변수 :  customer_sales

- 종속 변수 : gender, state, age or age_group, married, kids_under12, register_year



#### 예측 방안

------

- 고객별 특성을 대상으로 고객별 연간 매출 예측(annual_customer_sales) 및 vital Few 확인



#### 다중회귀분석

------

1. age-group dummy화

   (1) 전체 변수들 dummy화 진행 후 p-value가 유의하고 다중공선성 문제없는 변수 대상

   - R-squared :0.393

   - Adj. R-squared : 0.388
   - 대상 변수 : 28개

   (2) 후진 제거법

   ​	1) 변수 중요도가 높은 10개 선택

   ​		- R-squared :0.393

   ​        - Adj. R-squared : 0.381

   ​        - 대상 변수 : 9개(R-square가 영향을 받지 않는 선에서 p-value가 0.45로 높은 변수 삭제)

   ​	2)  변수 중요도가 높은 15개 선택

   ​		- R-squared :0.383

   ​		- Adj. R-squared : 0.381

   ​		- 대상 변수 : 9개(R-square가 영향을 받지 않는 선에서 p-value가 0.45로 높은 변수 삭제)

   

2. age 변수 연속형으로 분석

   - R-squared :0.367

   - Adj. R-squared : 0.365
   - 대상 변수 : 10개

   

3. 최종 모델

   - R-squared :0.394
   - Adj. R-squared : 0.392
   - 대상 변수 : 11개

   ![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcQAAAD4CAYAAABykJZ9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nO3de5BdVb3u/e8jCBwIRI+0HAU0ICKCQgIdgS2KgRgBL8AWhBQHQXhBQGVzLEqxFLy+Cht8QeQa2cgGORHQAwIiFyWAUCTSCSEh3MRAEENpI5xsLnKT5/1jjJbFsldndej06k4/n6qurB5zrDF/c3VRP8aYY82fbBMRETHWva7TAURERIwESYgREREkIUZERABJiBEREUASYkREBACrdzqAWHHrr7++J0yY0OkwIiJGlblz5z5uu6u5PQlxFJswYQI9PT2dDiMiYlSRtKS/9iyZRkREkIQYEREBJCFGREQAuYcYETGq7HLUI50O4TW58ay3dTqEljJDjIiIIAkxIiICSEL8B0nHSFp7qPq1eO/HJN0p6S5J90j6bMOxT0u6W9KieuzYFTlHRESsmCTEVxwDtJPo2u33KpJeD8wAPm57G2AScFM9tnsdd5rtrYBtgWWDPUdERKy4MZkQJa0j6Zd1pna3pK8DbwVmSZpV+5wtqafO2L5Z247up980SbdLmifpMknjWpx2Xcompr8C2H7e9v312FeAY20vrcees/2jFrEfXuPq6e3tHZLPIyIixmhCBHYDltrexvZ7gNOApcAU21Nqn6/a7ga2BnaWtLXt0xv7SVof+Bow1fa2QA/wxf5OaPsJ4EpgiaSZkg6Q1Pf5vweY207gtmfY7rbd3dX1T08eioiIFTRWE+JCYKqkkyR9wHZ/y5OfkjQPuBPYCtiynz471PbbJM0HDgLe3uqktv8fYFfgd8CxwPmv7TIiImKojMnvIdp+QNJ2wB7A9yRd33hc0iaUhDXZ9pOSLgDW6mcoATfYnj6Icy8EFkq6CHgIOBhYBGwH3LgClxMREUNgTM4QJb0VeNb2T4BTKJtYnqLc5wNYD3gGWCZpA2D3hrc39psNvF/SZnXctSVt3uKc4yR9qKFpItD3gNnvAf8u6X/UvmvW+5URETFMxuQMEXgvcLKkl4EXgSOBHYFfSXqs3h+8kzJzWwzc1vDeGU39DgZmSlqzHv8a8EA/5xTwJUnnAn+jJNyDAWxfUxPvryUJMFlOjYh+jOQnvYx2st3pGGIFdXd3O+WfIiIGR9LcumnyVcbkkmlERESzsbpkulJJuhzYpKn5y7av60Q8ERGxfEmIK4HtvTsdQ0REDE6WTCMiIkhCjIiIAJIQIyIigCTEiIgIIAkxIiICyC7TiBiBdjnqkU6HMGLlSTUrT2aIERERJCFGREQASYj9knSMpLWHql+L994k6X5Jd0m6Q9LEhmMP1+LDERExTJIQ+3cM0E6ia7dfKwfY3gY4Czj5NYwTERGv0ZhPiJLWkfTLOlO7W9LXgbcCsyTNqn3OltQjaZGkb9a2o/vpN03S7ZLmSbpM0rg2w7gd2LDNeA+vsfT09vYO9nIjIqKFMZ8Qgd2Apba3sf0e4DRgKTDF9pTa56u1VMjWwM6StrZ9emO/usT5NWCq7W2BHuCLg4jhinY62p5hu9t2d1dXV9sXGRERA8vXLmAhcIqkk4Crbf+21Oh9lU9JOpzyeb0F2BJY0NRnh9p+W33/GpSZ30AulrQOsBqw7Wu6ioiIeE3GfEK0/YCk7YA9gO9Jur7xuKRNgGOBybaflHQBsFY/Qwm4wfb0QZz+AOAu4ETgTOBfV+ASIiJiCIz5JVNJbwWetf0T4BTKTO0pYN3aZT3gGWCZpA2A3Rve3thvNvB+SZvVcdeWtPnyzm/7RcpS6w6S3j0ElxQREStgzM8QgfcCJ0t6GXgROBLYEfiVpMfq/cE7gUXAYuC2hvfOaOp3MDBT0pr1+NeAB5YXgO2/Sfo+ZSZ66FBdWMRolaexRCfIdqdjiBXU3d3tnp6eTocRETGqSJpbN0q+yphfMo2IiIAsma50ki4HNmlq/rLt6zoRT0RE9C8JcSWzvXenY4iIiOXLkmlERARJiBEREUASYkREBJCEGBERASQhRkREANllGhExquxy1COdDuFVVqWnCmWGGBERQRJiREQEkIQIgKRjJK09VP1avPcmST0Nv3fXtnUk/VXS+Kb+V0j61IqcKyIiBi8JsTgGaCfRtduvlTdLaiwfhe1ngOuBvfraanLcCbj6NZwrIiIGYcwlxDoj+6WkuyTdLenrwFuBWZJm1T5nS+qRtEjSN2vb0f30mybpdknzJF0madxyTn8ypSRUs5nA/g2/7w1ca/vZfuI/vMbW09vbO9jLj4iIFsZcQgR2A5ba3sb2e4DTgKXAFNtTap+v1tIgWwM7S9ra9umN/SStT0luU21vC/QAX1zOuW8Hnpc0pan9WmA7SW+qv+9PSZL/xPYM2922u7u6ugZ14RER0dpYTIgLgamSTpL0AdvL+unzKUnzgDuBrYAt++mzQ22/TdJ84CDg7W2c/zs0zRJtvwBcCexTE+1EyjJqREQMkzH3PUTbD0jaDtgD+J6kVyUeSZtQKtdPtv2kpAuAtfoZSsANtqcP8vw3Svo2JaE2mklJlAJ+YfvFwYwbERGvzZibIUp6K/Cs7Z8ApwDbAk8B69Yu6wHPAMskbQA0boJp7DcbeL+kzeq4a0vavM0w/l/gS01ts4B3Ap+jxXJpRESsPGNuhgi8FzhZ0svAi8CRwI7AryQ9Vu8P3gksAhYDtzW8d0ZTv4OBmZLWrMe/BjywvABsXyOpt6ntZUk/B/YFbnltlxgRq6pV6ckwI41sdzqGWEHd3d3u6elZfseIiPgHSXPrxslXGXNLphEREf0Zi0umK5Wky4FNmpq/bPu6TsQTERHtSUIcYrb37nQMERExeFkyjYiIIAkxIiICSEKMiIgAkhAjIiKAJMSIiAggu0zHrF2OeqTTIUTECsiTalaezBAjIiIYhoQo6ROSjhvg+ERJe6zsOIZafZj3LyXdVwsJn9hwbE1Jl0h6UNIcSRNq+5skzZL0tKQzmsabLmmhpAWSrq1loCIiYpgMKiGqGNR7bF9p+8QBukyklGIaTBzDttS7nGs+xfYWwCRK5Yu+yhiHAk/a3gw4FTiptj8HHE8pL9V4jtWBH1CKD28NLAA+P7RXEhERA1lucpM0QdK9ks4C5gEHSrpd0jxJl0kaV/vtUWdLt0o6XdLVtf3gvtmQpH0l3S3pLkm3SFoD+Bawn6T5kvaTtI6k8yXdIelOSXs2jHOZpKtoUTxX0kV9/evvF9cZ6mqSTq5jLpD02Xp8nKTf1GtZ2HCu5mveuPlctp+1Pau+fqH226ge3hP4z/r6Z8CukmT7Gdu3UhLjq0KvP+tIEqUE1dLl/W0iImLotDvbexdwIfBhyuxnqu1tgR7gi5LWAs4Fdre9E9DVYpwTgI/Y3gb4RE0kJwCX2J5o+xLgq8CNticDUyilmtap798ROMj2Li3GPw/4DICk8cC/ANfUmJfVMScDh9VCwM8Be9drmQJ8vyakf1yz7Um2lwz04Uh6A/Bx4De1aUPgjwC2XwKWAW9q9f5aDPhIYCElEW4J/EeLcx0uqUdST29vb39dIiJiBbSbEJfYnk2p8r4lcJuk+cBBwNuBLYDFth+q/VsVuL0NuEDSYcBqLfpMA46r499EqVbft63qBttPtArS9s3AZpLeDEwHfl4T0jTg03XMOZTk9E7KrOy7khYAv6Yksg2arnlAdblzJnC67cV9zf2FN8AYr6ckxEnAWylLpl9pcY0zbHfb7u7qavX/HRERMVjt3ot7pv4rSlKa3nhQ0qR2BrF9hKTtgY8C8yVN7KebgE/avr/pHNs3xDGQi4ADgP2BQxrG/EJzxYla4LcL2M72i5IepiRg2jwXlKLBv7d9WkPbo5Rl1kdrwhwPtEzklPuo2P5DjetSoOVGpIiIGHqD3WU6m7J5ZDP4x07LzYH7gE37dlMC+/X3ZknvsD3H9gnA45Sk8RSwbkO364Av9C1dtptsG1wAHANge1HDmEfWmRiSNq/LsOOBv9RkOIUy222bpO/UMY5pOnQlZfYMsA9lCXigSsx/AraU1Dfl+zBw72BiiYiI12ZQuzVt99ZZ1UxJa9bmr9l+QNJRwLWSHgd+12KIkyX1LVX+BrgLeIRXlki/B3wbOA1YUJPiw8DHBhHjnyXdC1zR0HweMAGYV8fsBfYCLgauktQDzKck9rZI2ohyv/O+Oi7AGbbPo9z/u0jSg5SZ4f4N73uYsmlmDUl7AdNs3yPpm8Atkl4ElgAHtxvLisiXeyMiXk0DT1wGMZA0zvbTNeGcSVlGPHVIBh9cHGtTNqdsa3vZcJ9/OHV3d7unp6fTYUREjCqS5trubm4fyi/mH1ZneYsoy4jnDuHYbZE0lTJj++GqngwjImJoDdkX3OtscFhmhJLeS9k80+h529vzyo7UoTzfHGDNpuYDbS8c6nNFRERnjMqHe9dE1N8O1ZV1vu2H61wREdEZebh3REQESYgRERFAEmJERASQhBgREQEkIUZERACjdJdprPp2OeqRTocQMSLlKVMrT2aIERERJCFGREQAw5AQa8X6lqWMJE2UtMfKjmOo1Uofv5R0n6RFkk5sOLampEskPShpTl8VEElvkjRL0tOSzmjov66k+Q0/j0s67Z/PGhERK8ugEqKKQb3H9pW2Txygy0RgUAmx1hgcFsu55lNsb0Ep7Pt+SbvX9kOBJ21vRnmc3Um1/TngeODYxkFsP2V7Yt8PpdrF/xnqa4mIiNaWm9wkTZB0r6SzgHnAgZJulzRP0mWSxtV+e9TZ0q2STpd0dW0/uG82JGlfSXdLukvSLZLWAL4F7FdnRvtJWkfS+ZLukHSnpD0bxrlM0lXA9S1ivaivf/394jpDXU3SyXXMBZI+W4+Pk/Sbei0LG87VfM0bN5/L9rO2Z9XXL9R+G9XDewL/WV//DNhVkmw/Y/tWSmJs9Xm/E3gz8NsWxw+X1COpp7e3t9UwERExSO3O9t4FXEgpXHsoMNX2tkAP8EVJa1GqW+xueydKFfr+nAB8xPY2wCdqIjkBuKTOji6h1Bi80fZkYAqlhuI69f07AgfZ3qXF+OcBnwGQNB74F+CaGvOyOuZkSmWOTSiJae96LVOA79fyVf+4ZtuTbC8Z6MOR9Abg45QajwAbAn8EsP0SsAx400BjNJheP49+63LZnmG723Z3V1erjzkiIgar3YS4xPZsYAdgS+C2WurpIEqV+S2AxbYfqv1nthjnNuACSYcBq7XoM41XCgbfBKzFKxUsbrD9RKsgbd8MbCbpzZTE8vOakKYBn65jzqEkp75Cxd+VtAD4NSWRbdB0zQOqy7czgdNtL+5r7i+85Y1V7U/rzy8iIlaSdu/FPVP/FSUpTW88KGlSO4PYPkLS9sBHgfmS+qtYIeCTtu9vOsf2DXEM5CLgAEpiOaRhzC/Yvq5pzIMps9ntbL9Yq9mvVQ+3cy6AGZRiyI2bYB6lLLM+WhPmeKBlIm+IZxtgddtz2zx3REQMkcHuMp1N2TyyGfxjp+XmlKK8m/btpgT26+/Nkt5he47tE4DHKUnjKWDdhm7XAV/oW7psN9k2uAA4BsD2ooYxj5T0+jrm5nUZdjzwl5oMp1Bmu22T9J06xjFNh66kzJ4B9qEsAbczQ5xOZocRER0xqN2atnvrrGqmpL6CuV+z/YCko4BrJT0O/K7FECfXTSOi3G+7C3iEV5ZIvwd8GzgNWFCT4sPAxwYR458l3Qtc0dB8HjABmFfH7AX2Ai4GrpLUA8ynJPa2SNqIcr/zvjouwBm2zwP+A7hI0oOUmeH+De97GFgPWEPSXsA02/fUw59ikDtuV1V5GkdEDDe1N3FpYyBpnO2na8I5k7KMeOqQDD64ONYGFgLb2l423OcfTt3d3e7p6el0GBERo4qkuba7m9uH8ov5h9VZ3iLKMuK5Qzh2WyRNpczYfriqJ8OIiBhaQ/YF9zobHJYZoaT3UjbPNHre9va8siN1KM83B1izqflA2wuH+lwREdEZo7LaRU1E/e1QXVnn2364zhUREZ2Rh3tHRESQhBgREQEkIUZERABJiBEREUASYkREBDBKd5lGdMouRz3S6RBijMtTnFaezBAjIiJIQoyIiACGISHWivXHDXB8oqRR90DrWunjl5Luk7RI0okNx9aUdImkByXN6asCIulNkmZJelrSGU3jrSFphqQH6pifHN4riogY2waVEFUM6j22r7R94gBdJjLICg+1xuCwWM41n2J7C2ASpSzW7rX9UOBJ25tRHmd3Um1/DjgeOLafsb5KKUW1OaUI881DdQ0REbF8y01ukiZIulfSWcA84EBJt0uaJ+kySeNqvz3qzOZWSadLurq2H9w3G5K0r6S7Jd0l6RZJawDfAvaTNF/SfpLWkXS+pDsk3Slpz4ZxLpN0FXB9i1gv6utff7+4zlBXk3RyHXOBpM/W4+Mk/aZey8KGczVf88bN57L9rO1Z9fULtd9G9fCewH/W1z8DdpUk28/YvpWSGJsdQil/he2XbT/e4hoPl9Qjqae3t7e/LhERsQLane29C7gQ+DBl9jPV9rZAD/BFSWtRqlvsbnsnShX6/pwAfMT2NsAnaiI5AbjE9kTbl1BmSjfangxModRQXKe+f0fgINu7tBj/POAzAJLGA/8CXFNjXlbHnEypzLEJJTHtXa9lCvD9vsLEfddse5LtJQN9OJLeAHycUuMRYEPgjwC2XwKWAW9azvsBvt3wPxob9NfX9gzb3ba7u7pafcwRETFY7SbEJbZnAztQlvNuq6WeDqJUmd8CWGz7odq/VdX324ALJB0GrNaizzReKRh8E7AWr1SwuMH2E62CtH0zsJmkN1Oqz/+8JqRpwKfrmHMoyamvUPF3JS0Afk1JZH2JqO+aB1SXb2cCp9te3NfcX3gDDLM6ZXZ5W03OtwOnLO/cERExdNq9F/dM/VeUpDS98aCkSe0MYvsISdsDHwXmS+qvYoWAT9q+v+kc2zfEMZCLgAMoVeoPaRjzC7avaxrzYMpsdjvbL9Zq9mvVw+2cC2AGpRjyaQ1tj1KWWR+tCXM80DKRA38FngUur79fRpnVRkTEMBnsLtPZlM0jm8E/dlpuTinKu2nfbkpgv/7eLOkdtufYPgF4nJI0ngLWbeh2HfCFvqXLdpNtgwuAYwBsL2oY80hJr69jbl6XYcdTNrK8KGkKZbbbNknfqWMc03ToSsrsGWAfyhJwyxliPXYV8KHatCtwz2BiiYiI12ZQuzVt99ZZ1UxJfQVzv2b7AUlHAddKehz4XYshTpbUt1T5G+Au4BFeWSL9HvBt4DRgQU2KDwMfG0SMf5Z0L3BFQ/N5wARgXh2zF9gLuBi4SlIPMJ+S2NsiaSPK/c776rgAZ9g+D/gP4CJJD1Jmhvs3vO9hYD1gDUl7AdNs3wN8ub7ntBrfZ9qNJYZPnhISserSABOXwQ0kjbP9dE04Z1KWEU8dksEHF8fawEJgW9vLhvv8w6m7u9s9PT2dDiMiYlSRNNd2d3P7UH4x/7A6y1tEWUY8dwjHboukqZQZ2w9X9WQYERFDa8i+4F5ng8MyI5T0XsrmmUbP296eV3akDuX55gBrNjUfaHvhUJ8rIiI6Y1RWu6iJqL8dqivrfNsP17kiIqIz8nDviIgIkhAjIiKAJMSIiAggCTEiIgJIQoyIiABG6S7TiFg17XLUI50OYcTL05JWnswQIyIiSEKMiIgAhiEh1or1xw1wfKKkPVZ2HEOtVvr4paT7JC2SdGLDsTUlXSLpQUlz+qqASHqTpFmSnpZ0RtN4N0m6X9L8+vPm4b2iiIixbVAJUcWg3mP7StsnDtBlIjCohFhrDA6L5VzzKba3ACZRymLtXtsPBZ60vRnlcXYn1fbngOOBY1uMd4DtifXnL0N0CRER0YblJjdJEyTdK+ksYB5woKTbJc2TdJmkcbXfHnW2dKuk0yVdXdsP7psNSdpX0t2S7pJ0i6Q1gG8B+9VZ0X6S1pF0vqQ7JN0pac+GcS6TdBVwfYtYL+rrX3+/uM5QV5N0ch1zgaTP1uPjJP2mXsvChnM1X/PGzeey/aztWfX1C7XfRvXwnsB/1tc/A3aVJNvP2L6VkhhXiKTDJfVI6unt7V3RYSIiokm7s713ARcCH6bMfqba3hboAb4oaS1KdYvdbe9EqULfnxOAj9jeBvhETSQnAJfUWdEllBqDN9qeDEyh1FBcp75/R+Ag27u0GP88ah1BSeOBfwGuqTEvq2NOplTm2ISSmPau1zIF+H5fYeK+a7Y9yfaSgT4cSW8APk6p8QiwIfBHANsvAcuANw00RvXj+j8GxzfE8Sq2Z9jutt3d1dXqY46IiMFqNyEusT0b2AHYEritlno6iFJlfgtgse2Hav+ZLca5DbhA0mHAai36TOOVgsE3AWvxSgWLG2w/0SpI2zcDm9X7b9OBn9eENA34dB1zDiU59RUq/q6kBcCvKYlsg6ZrHlBdvp0JnG57cV9zf+EtZ6gDbL8X+ED9OXB5546IiKHT7r24Z+q/oiSl6Y0HJU1qZxDbR0jaHvgoMF9SfxUrBHzS9v1N59i+IY6BXAQcQKlSf0jDmF+wfV3TmAdTZrPb2X6xVrNfqx5u51wAMyjFkE9raHuUssz6aE2Y44GWiRzA9p/qv09J+t/A+yiz8oiIGAaD3WU6m7J5ZDP4x07LzSlFeTft200J7NffmyW9w/Yc2ycAj1OSxlPAug3drgO+0Ldk2G6ybXABcAyA7UUNYx4p6fV1zM3rMux44C81GU6hzHbbJuk7dYxjmg5dSZk9A+xDWQJuOUOUtLqk9evr1wMfA+4eTCwREfHaDGq3pu3eOquaKamvYO7XbD8g6SjgWkmPA79rMcTJkvqWKn8D3AU8witLpN8Dvg2cBiyoSfFhSoJoN8Y/S7oXuKKh+TxgAjCvjtkL7AVcDFwlqQeYT0nsbZG0EeV+5311XIAzbJ8H/AdwkaQHKTPD/Rve9zCwHrCGpL0oy7lLgOtqMlyNsnz7o3ZjiVhV5Cks0UkaYOIyuIGkcbafrgnnTMoy4qlDMvjg4lgbWAhsa3vZcJ9/OHV3d7unp6fTYUREjCqS5trubm4fyi/mH1ZneYsoy4jnDuHYbZE0lTJj++GqngwjImJoDdkX3OtscFhmhJLeS9k80+h529vzyo7UoTzfHGDNpuYDbS8c6nNFRERnjMpqFzUR9bdDdWWdb/vhOldERHRGHu4dERFBEmJERASQhBgREQEkIUZERABJiBEREcAo3WUaETFW7XLUI50OYaUYCU8pygwxIiKCJMSVStLWtZjyolqAeK3avl39/cFaTLnf2ocRETF8xmRCVLFSr72WffoJcITtrYAPAS/Ww2cDh1NqMr4T2G1lxhIREcvXsYQo6QpJc+vs6fDadqikByTdJOlHks6o7V2Sfi7pjvrz/gHG7ZJ0g6R5ks6VtETS+pImSLpX0lnAPGBjSdPrTO1uSSc1jPF0w+t9JF1QX18g6RxJv61xDlSFYxqwwPZdALb/avvvkt4CrGf79loS6kJK5Q0kHS3pHkkLJP10xT7ZiIhYEZ2cIR5iezugGzha0obA8cAOwIeBLRr6/gA41fZk4JOUck6tfJ1Sf3Bb4HJe/WzTdwEX2p5Ema2dBOxCeQzc5FqOaXkmADtTihyf07cM2o/NAUu6ribnL9X2DSkFhPs8WtsAjgMm2d4aOKK/QSUdLqlHUk9vb28b4UZERDs6mRCPlnQXpejwxsCBwM22n7D9InBZQ9+pwBm1msaVwHqS1v2nEYudgJ8C2L4WeLLh2BLbs+vrycBNtnttv0SpjfjBNuK+1PbLtn8PLObVibvR6jWWA+q/e0valVILsllfDa4FwMWS/ifwUn+D2p5hu9t2d1dXVxvhRkREOzqSECV9iJLkdrS9DXAncP8Ab3ld7Tux/mxo+6lWww8wzjNt9mssEtk8A2wuINmqoOSjlAT/uO1ngWuAbWv7Rg39NgKW1tcfpdSS3A6YW+9DRkTEMOjUDHE88KTtZyVtQVkmXRvYWdIbayL4ZEP/64HP9/0iaaBKF7cCn6r9pgFvbNFvTj3f+pJWA6YDN9djf5b07rrxZu+m9+0r6XWS3gFsSutEfh2wtaS16/XsDNxj+zHgKUk71N2lnwZ+Uc+1se1ZwJeANwDjBrjOiIgYQp2agVwLHCFpASWhzAb+BHyXkqiWAvcAfUV+jwbOrP1XB26hxT024JvATEn7URLcY8BTNCUX249J+gowizJbvMb2L+rh44CrgT8Cdze99/467gaUHaTP9ReE7Scl/X/AHZRZ5DW2f1kPHwlcAPw34Ff1Z3XgJ5LG13hOtf1/W1xjREQMMZWNjiODpHG2n64zqsuB821fPsgx1gT+bvslSTsCZ9sektqJdbfp1bZ/NhTjvVbd3d3u6enpdBgREaOKpLm2u5vbR9o9qm9Imkq5b3c9cMUKjPE24NK6BPkCcNgQxhcREauoEZUQbR/bbl9JnwH+ran5NtufAyYNaWCV7YP7ieMjlK9vNHrIdvO9x4iIGMFGVEIcDNs/Bn48AuK4jrKBJiIiRrEx+ei2iIiIZkmIERERJCFGREQASYgRERFAEmJERAQwineZRkSMRbsc9UinQ3hNbjzrbcvv1CGZIUZERJCEGBERASQhrjSSJkj6m6T59eechmPbSVoo6UFJp9eqFxER0UFj8h5iTUCy/fJKPtUfWjxY/GzgcEqVj2uA3SgVLyIiokM6NkOUdIWkuZIWSTq8th0q6QFJN0n6kaQzanuXpJ9LuqP+vH+Acbsk3SBpnqRzJS2pNQ8nSLpX0lnAPGBjSdPrTO1uSSc1jPF0w+t9apULJF0g6RxJv61xfmwFrvstwHq2b3cpNXIhsFc9drSkeyQtkPTTFu8/XFKPpJ7e3t7Bnj4iIlro5JLpIba3A7qBoyVtCBxPKRb8YWCLhr4/oNQHnEwpHHzeAON+HbjR9raUElKNW5reBVxoexLwIuWh3LsAE4HJkvZqI+4JlGK/HwXOkbTWAH03kXSnpJslfaC2bQg82tDn0doGpQ7jJNtb025MBxwAAA4CSURBVKLeo+0Ztrttd3d1dbURbkREtKOTS6ZHS+qrCLExcCBws+0nACRdBmxej08Ftmy41baepHVtP9XPuDtRq9zbvlbSkw3HltieXV9PBm6y3VvPdzHwQZZfcurSutT6e0mLKYl7fj/9HgPeZvuvkrYDrpC0FaX4b7O+opQLgIslXdFGHBERMYQ6khAlfYiS5Ha0/aykmyiV6N/d4i2vq33/1s7wAxx7ps1+jVWTm2eAzRWV+62wbPt54Pn6eq6kP1AS/KPARg1dNwKW1tcfpSTlTwDHS9rK9ksDxBkREUOkU0um44EnazLcgrJMujaws6Q3SlqdsjTa53rg832/SOpvo0qfW4FP1X7TgDe26Dennm99SasB04Gb67E/S3p3LTLcXNdwX0mvk/QOYFNKIv8n9V7mavX1psA7gcW2HwOekrRD3dzzaeAX9Vwb254FfAl4AzBugOuMiIgh1Kkl02uBIyQtoCSU2cCfgO9SEtVS4B5gWe1/NHBm7b86cAst7rEB3wRmStqPkuAeA56iKbnYfkzSV4BZlNniNbZ/UQ8fB1wN/BG4u+m999dxNwCOsP1cizg+CHxL0kvA32vfJ+qxI4ELgP9G2V36q3pdP5E0vsZzqu3/22LsiBijRvKTXkY7lY2OI4OkcbafrjPEy4HzbV8+yDHWBP5u+yVJOwJnt/jqw4rEdwFwte2fDcV4r1V3d7d7eno6HUZExKgiaa7t7ub2kfY9xG9Imkq5b3c9K7ax5G3ApXUJ8gXgsCGMLyIiVlEjKiHaPrbdvpI+A/xbU/Nttj8HTBrSwCrbB/cTx0coX99o9JDt5nuPERExgo2ohDgYtn8M/HgExHEdcF2n44iIiNcmzzKNiIggCTEiIgJIQoyIiACSECMiIoAkxIiICGAU7zKNiBiLdjnqkU6H0HEr62k9mSFGRESQhBgREQEkIa50kt4m6WlJxza07SbpfkkPSjquk/FFREQxJhOiiuG69lMp1Sz6zr0acCawO7AlMF3SlsMUS0REtNCxhCjpCklzJS2SdHhtO1TSA5JukvQjSWfU9i5JP5d0R/15/wDjdkm6QdI8SedKWlJrHk6QdK+ks4B5wMaSpktaKOluSSc1jPF0w+t9apULJF0g6RxJv61xfmw517gXsBhY1ND8PuBB24ttvwD8FNiz9j9R0j2SFkg6pcWYh0vqkdTT29s70OkjImIQOjlDPMT2dkA3cLSkDYHjKcWCPwxs0dD3B5T6gJMphYPPG2DcrwM32t6WUkKqcTvSu4ALbU8CXqQ8lHsXYCIwuSaw5ZkA7Eypbn+OpLX66yRpHeDLlPqMjTak1Fns8yiwoaT/TilGvJXtrYHv9Deu7Rm2u213d3V1tRFuRES0o5MJ8WhJd1GKA28MHAjcbPsJ2y8ClzX0nQqcIWk+cCWwnqR1W4y7E2XWhe1rgScbji2xPbu+ngzcZLvX9kvAxZSivstzqe2Xbf+eMvvbokW/b1KS+NNN7eqnr4H/Ap4DzpP0r8CzbcQSERFDpCPfQ5T0IUqS29H2s5JuolSif3eLt7yu9v1bO8MPcOyZNvs1Vk1ungE2V1RuVWF5e2AfSf8OvAF4WdJzwFzK/wD02QhYWgsavw/YFdgf+Dxl9hoREcOgUzPE8cCTNRluQVkmXRvYWdIbJa1OWRrtcz0lQQAgaeIAY98KfKr2mwa8sUW/OfV869eNLtOBm+uxP0t6d91401zXcF9Jr5P0DmBTSiL/J7Y/YHuC7QnAacB3bZ8B3AG8U9ImktagJL8rJY0Dxtu+BjiGsowbERHDpFNPqrkWOELSAkpCmQ38CfguJVEtBe4BltX+RwNn1v6rA7cAR7QY+5vATEn7URLcY8BTwLjGTrYfk/QVYBZltniN7V/Uw8cBV1Pu9d3d9N7767gbAEfYfm4wF15ngp+n1FBcDTjf9iJJbwF+Ue9JCvhfgxk3IsaGlfWUlgDZrVb8hp+kcbafrjPEyynJ4vJBjrEm8PeaeHYEzrY9JLOtutv0ats/G4rxXqvu7m739PR0OoyIiFFF0lzb3c3tI+1Zpt+QNJVy3+564IoVGONtwKV1ufMF4LAhjC8iIlZRIyoh2j52+b0KSZ8B/q2p+TbbnwMmDWlgle2D+4njI5SvbzR6yHbzvceIiBjBRlRCHAzbPwZ+PALiuI5yPzAiIkaxMfnotoiIiGZJiBERESQhRkREAEmIERERQBJiREQEMIp3mUZEjEW7HPVIR847Fp6QkxliREQESYgRERFAEuJKI+l9kubXn7sk7d1wbDdJ90t6UNJxnYwzIiKKMXkPUZIoDzZ/eSWe5m6guz5k/C3AXZKuotRPPBP4MPAocIekK23fsxJjiYiI5ejYDFHSFZLmSlok6fDadqikByTdJOlHks6o7V2Sfi7pjvrz/gHG7ZJ0g6R5ks6VtKTWPJwg6V5JZwHzgI0lTZe0UNLdkk5qGOPphtf71CoXSLpA0jmSflvj/FirOGw/a/ul+utavFJI+H3Ag7YX234B+CmwZx3/REn3SFog6ZQW13e4pB5JPb29vcv5lCMiol2dXDI9xPZ2QDdwtKQNgeMpxYI/DGzR0PcHwKm2J1MKB583wLhfB260vS2lhFTj1qh3ARfangS8SHko9y6UYryTJe3VRtwTgJ2BjwLn1PqF/ZK0vaRFwEJK7cSXgA0pdRb7PApsKOm/U4oRb2V7a+A7/Y1pe4btbtvdXV1dbYQbERHt6GRCPFrSXZTiwBsDBwI3237C9ovAZQ19pwJnSJoPXAmsJ2ndFuPuRJl1Yfta4MmGY0tsz66vJwM32e6tiepi4INtxH2p7Zdt/x5YzKsT96vYnmN7q3qurzQU//2nrsB/Ac8B50n6V+DZNmKJiIgh0pF7iJI+RElyO9p+VtJNlEr0727xltfVvn9rZ/gBjj3TZr/GqsnNM8DmisrLrbBs+15JzwDvocwIN244vBGwtN5rfB+wK7A/8HnK7DUiIoZBp2aI44EnazLcgrJMujaws6Q3SlqdsjTa53pKggBA0sQBxr4V+FTtNw14Y4t+c+r51pe0GjAduLke+7Okd9ciw811DfeV9DpJ7wA2pSTyfyJpk3odSHo7Zbn2YeAO4J31+BqU5HelpHHAeNvXAMdQlnEjImKYdGqX6bXAEZIWUBLKbOBPwHcpiWopcA+wrPY/Gjiz9l8duAU4osXY3wRmStqPkuAeA54CxjV2sv2YpK8AsyizxWts/6IePg64mnKv7+6m995fx92Acl/wuRZx7AQcJ+lF4GXgKNuPA0j6PKWG4mrA+bYX1Z2ov2hYVv1fLcaNiDFsLDwxplNkL3fFb9hIGmf76TqzupySLC4f5BhrAn+vS5A7AmfbHpLZVt1terXtnw3FeK9Vd3e3e3p6Oh1GRMSoImmu7e7m9pH2PcRvSJpKuW93PXDFCozxNuDSutz5AnDYEMYXERGrqBGVEG0f225fSZ8B/q2p+TbbnwMmDWlgle2D+4njI5SvbzR6yHbzvceIiBjBRlRCHAzbPwZ+PALiuI5yPzAiIkaxEXUPMQZHUi+wZBBvWR94fCWFMxxGe/ww+q8h8XfeaL+GkRD/223/05NNkhDHEEk9/d1IHi1Ge/ww+q8h8XfeaL+GkRx/ql1ERESQhBgREQEkIY41MzodwGs02uOH0X8Nib/zRvs1jNj4cw8xIiKCzBAjIiKAJMSIiAggCXGVJ+lkSfdJWiDpcklvqO0TJP1N0vz6c06nY22l1TXUY1+R9KCk++tTg0YcSftKWiTpZUndDe2j6W/Q7zXUYyP+b9BI0jck/anhc9+j0zG1Q9Ju9TN+UNJxnY5nRUh6WNLC+rmPuAcxJyGu+m4A3mN7a+AB4CsNx/5ge2L9aVU9ZCTo9xokbUkpn7UVsBtwVi3lNdLcDfwrpUpLs9HyN+j3GkbR36DZqQ2f+zWdDmZ56md6JrA7sCUwvX72o9GU+rmPuO8iJiGu4mxfb/ul+utsSkHiUWWAa9gT+Knt520/BDwIvK8TMQ7E9r22+62bOVoMcA2j4m+wCngf8KDtxbZfAH5K+exjCCUhji2HAL9q+H0TSXdKulnSBzoV1CA1XsOGlJqVfR6tbaPJaPwbNBqtf4PP1yX48yW1KiI+kozWz7mZgeslzZV0eKeDaTZqH+4dr5D0a+B/9HPoq31FjyV9FXgJuLgeewx4m+2/StoOuELSVrb/a1iCbrKC16B++nfke0TtxN+PUfc36O9t/bR1/LtcA10LcDbwbUqc3wa+T/kfrZFsRH7OK+D9tpdKejNwg6T7bPd3K6EjkhBXAbanDnRc0kHAx4BdXb94avt54Pn6eq6kPwCbAx250b0i10D5v+SNG7ptBCxdOREObHnxt3jPqPobtDBi/gaN2r0WST8Crl7J4QyFEfk5D5btpfXfv0i6nLIUPGISYpZMV3GSdgO+DHzC9rMN7V19mx8kbQq8E1jcmSgH1uoagCuB/SWtKWkTyjX8rhMxrojR9DcYwKj7G0h6S8Ove1M2DI10dwDvlLSJpDUoG5mu7HBMgyJpHUnr9r0GpjHCPvvMEFd9ZwBrUpYnAGbX3YwfBL4l6SXg78ARtp/oXJgD6vcabC+SdClwD2Up9XO2/97BOPslaW/gh0AX8EtJ821/hFH0N2h1DaPlb9Dk3yVNpCw5Pgx8trPhLJ/tlyR9nlJ7dTXgfNuLOhzWYG0AXF7/G14d+N+2r+1sSK+WR7dFRESQJdOIiAggCTEiIgJIQoyIiACSECMiIoAkxIiICCAJMSIiAkhCjIiIAOD/B+Kkmn9ZbwXBAAAAAElFTkSuQmCC)

   

   

   

   #### Tree Models

   ------

   1. DecisionTree

      - test score : 0.352
   
      |            Feature | Importance |
      | -----------------: | ---------- |
      | register_year_2017 | 0.494      |
      | register_year_2016 | 0.350      |
      | register_year_2015 | 0.106      |
      |           state_SC | 0.027      |
   |           state_NV | 0.021      |
      |      age_group_40s | 0.001      |

   2. RandomForest

      - test score : 0.381
   
      |            Feature | Importance |
      | -----------------: | ---------- |
      | register_year_2017 | 0.404      |
      | register_year_2016 | 0.286      |
      | register_year_2015 | 0.087      |
      |      age_group_20s | 0.051      |
      |           state_NV | 0.033      |
      |           state_SC | 0.024      |
      |            married | 0.019      |
      |             gender | 0.018      |
   |      age_group_60s | 0.011      |
      |      age_group_40s | 0.011      |

   3. GradientBoosting

      - test score : 0.384
   
      |            Feature | Importance |
      | -----------------: | ---------- |
      | register_year_2017 | 0.409      |
      | register_year_2016 | 0.287      |
      | register_year_2015 | 0.085      |
      |      age_group_20s | 0.039      |
      |           state_NV | 0.032      |
      |           state_SC | 0.025      |
   | register_year_2018 | 0.014      |
      |      age_group_40s | 0.013      |

   

   #### 모델 평가

   ------

   - 대상 모델 : 다중회귀분석, DecisionTree, RandomForest, GradientBoosting
   
   |          | **회귀** | **DT** | **RF** | **GB** |
   | -------- | -------- | ------ | ------ | ------ |
   | **Mse**  | 120.2    | 126.5  | 122.52 | 123.4  |
   | **Rmse** | 10.9     | 11.2   | 11.06  | 11.1   |
   | **Mae**  | 8.3      | 8.7    | 8.3    | 8.2    |
   | **mape** | 835.2    | 871.8  | 829.1  | 823.8  |

- 모델 평가에 있어 가장 일반적이고 자주 사용되는 Rmse 기준으로 다중회귀모델을 선택하기로 결정