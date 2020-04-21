def mean_and_var(*val):
    # 평균 구하기
    vecSize = len(val[0])
    mean = [0 for i in range(vecSize)]
    for vec in val:
        for index, value in enumerate(vec):
            mean[index] += value
    mean = [ value/vecSize for value in mean ]
    
    # 분산 구하기
    
    var = [0 for i in range(vecSize)]
    for vec in val:
        for index, value in enumerate(vec):
            var[index] += (value - mean[index])**2
            
    var = [value/vecSize for value in var]
    
    return (mean, var)
    
    
def main():
    v1 = (0, 1)
    v2 = (0.5, 0.5)
    v3 = (1, 0)
    
    m, var = mean_and_var(v1, v2, v3)
    print('평균: ', m, '분산: ', var)
    
if __name__ == "__main__":
    main()