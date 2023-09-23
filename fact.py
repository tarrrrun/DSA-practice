def facct(n):
    res = 1
    for i in range (2,n+1):
        res = res * i
    return res
if __name__ == '__main__':
    num = 5
    print(facct(num))