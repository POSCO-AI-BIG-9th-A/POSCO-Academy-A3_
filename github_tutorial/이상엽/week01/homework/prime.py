def check_prime(num):
    for i in range(2, int(num/2)):
        if num%i == 0:
            return False
        
    return True
def main():
    a = 13
    b = 15
    if check_prime(a):
        print(str(a) + '는 소수입니다.')
    else:
        print(str(a) + '는 소수가 아닙니다.')

    if check_prime(b):
        print(str(b) + '는 소수입니다.')
    else:
        print(str(b) + '는 소수가 아닙니다.')
        
if __name__ == "__main__":
    main()
