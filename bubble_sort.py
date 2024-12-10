def bubbleSort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def optimisedCode(l):
    n=len(l)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
        if swapped==False:
            return
    return l


l=[5,21,3,12,11]
print(bubbleSort(l))
optimisedCode(l)
print(*l)