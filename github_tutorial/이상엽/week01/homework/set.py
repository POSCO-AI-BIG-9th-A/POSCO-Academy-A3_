class Set:
    def __init__(self, member=[]):
        tmp = []
        for x in member:
            if x not in tmp:
                tmp += [x]
        
        self.member = tmp
        
    def append(self, a):
        if a not in self.member :
            self.member += [a]
            
    def delete(self, a):
        if a in self.member :
            self.member.remove(a)
            
    def union(self, s2):
        new = Set(self.member[:])
        for x in s2.member:
            new.append(x)
        return new
    
    def intersection(self, s2):
        new = Set(self.member[:])
        for x in new.member:
            if x not in s2.member:
                new.delete(x)
        return new
    
    def difference(self, s2):
        new = Set(self.member[:])
        for x in s2.member:
            if x in new.member:
                new.delete(x)
        return new
    
    def __repr__(self):
        return str(self.member)
    
    def __add__(self, s2):
        return self.union(s2)
        
    def __sub__(self, s2):
        return self.difference(s2)
        
    def __truediv__(self, s2):
        return self.intersection(s2)
        

def main():
    a = Set([1, 2, 3])
    b = Set([2, 3, 4])
    
    c = a.union(b)
    print(c)
    d = a.difference(b)
    print(d)
    e = a.intersection(b)
    print(e)
    c = a + b
    print(c)
    d = a - b
    print(d)
    e = a / b
    print(e)
    
if __name__ == '__main__':
    main()