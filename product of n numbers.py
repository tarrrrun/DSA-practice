n = int(input("Give number: "))
product=0
if n==1:
    product=0
else:
    while n!=0:
        s = n-1
        product = n*s
print(product)