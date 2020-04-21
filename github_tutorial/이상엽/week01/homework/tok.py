def tokenize(trg, N=1):
    arr = trg.split(' ')
    if N is 1:
        return arr
    else:
        res = []
        if N < len(arr):
            for i in range(len(arr) - N + 1):
                tmp = ''
                for j in range(i, i+N):
                    tmp += arr[j] + ' '
                res.append((tmp.strip()))
                
        else:
            res.append(trg)
        return res
    
def main():
    a = "There was a farmer who had a dog ."
    print(tokenize(a))
    print(tokenize(a,2))
    
if __name__ == "__main__":
    main()
