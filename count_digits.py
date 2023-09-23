n = int(input("Give number: "))
res = 0
while n>0:
    n=n//10
    res = res+1
print(res)