
def primaya(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
        

def primeX(x):
    hasil = []
    for i in range (2, 100):
        if primaya(i):
            hasil.append(i)
    return hasil [x - 1]
    

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29