# def selectionSort(l):
#     n=len(l) #6
#     print(n)
#     for i in range(n-1):    # 0-4
#         min_ind=i
#         for j in range(i+1,n):  # 1-5
#             if l[j]<l[min_ind]:
#                 min_ind=j
#         l[i],l[min_ind]=l[min_ind],l[i]
#     return l

##########  SELECTION SORT IS NOT STABLE    #############

def selectionSort(l):
    n=len(l)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if l[j]<l[min_ind]:
                min_ind=j
        l[i],l[min_ind]=l[min_ind],l[i]
    return l
    
l=[8,6,5,4,2,1]
print(selectionSort(l))