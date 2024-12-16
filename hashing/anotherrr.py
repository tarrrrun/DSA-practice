def maxIndexDiff(arr):    
    l=[]
    ll=len(arr)
    for i in range(ll):
        num=0
        for j in range(1,i):
            if (arr[i]<=arr[j]) and i<=j:
                num=i-j
                l.append(num)
    if len(l) !=0:
        return max(l)
    elif 
arr=1,10
print(maxIndexDiff(arr))