import numpy as np

def randFn():
    return np.random.rand(2,2), np.random.rand(2)

 

if __name__=="__main__":
    x1 = np.array([0,0])
    x2 = np.array([0,1])
    x3 = np.array([1,0])
    x4 = np.array([1,1])
    
    checkFn = lambda a : np.argmax(a)
    while True:
        W, b = randFn()
      
    
        if checkFn(W.dot(x1) + b) != 0:
            continue
        elif checkFn(W.dot(x2) + b) != 0:
            continue
        elif checkFn(W.dot(x3) + b) != 0:
            continue
        elif checkFn(W.dot(x4) + b) != 1:
            continue
        else:
#             print(W)
#             print(b)
            print("f(W · x1 + b) = ", checkFn(W.dot(x1) + b))
            print("f(W · x2 + b) = ", checkFn(W.dot(x2) + b))
            print("f(W · x3 + b) = ", checkFn(W.dot(x3) + b))
            print("f(W · x4 + b) = ", checkFn(W.dot(x4) + b))
            break
    