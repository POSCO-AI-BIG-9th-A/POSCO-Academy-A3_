def add_comma(val):
    res = ""
    while val != 0:
        tmp = str(int(val % 1000))
        res = tmp + ',' + res
        val = int(val / 1000)
    
    return res.strip(',')

def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_12 = add_comma(12)
    
    print(comma_added_1234)
    print(comma_added_12345678)
    print(comma_added_12)
    
if __name__ == "__main__":
    main()