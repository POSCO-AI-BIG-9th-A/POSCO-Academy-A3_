def mean_and_var(*val):
    # 평균 구하기
    mean = [ sum(v)/len(val) for v in zip(*val)]

    # 분산 구하기
    var = []
    for i, v in enumerate(zip(*val)):
        tmp = 0
        for x in v:
            tmp += (x - mean[i])**2
        var.append(tmp / len(val))
                   
    return mean, var       

def main():
    v1 = (0, 1)
    v2 = (0.5, 0.5)
    v3 = (1, 0)
    
    m, var = mean_and_var(v1, v2, v3)
    print('평균: ', m, '분산: ', var)
    
if __name__ == "__main__":
    main()