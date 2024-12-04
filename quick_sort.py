def lomuto_partition(arr,l,h):
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def sortByLomuto(arr,l,h):
    if l<h:
        p=lomuto_partition(arr,l,h)
        sortByLomuto(arr,l,p-1)
        sortByLomuto(arr,p+1,h)
    return arr

def pracLomuto(arr,l,h):
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def pracQSort(arr,l,h):
    if l<h:
        p = pracLomuto(arr,l,h)
        pracQSort(arr,l,p-1)
        pracQSort(arr,p+1,h)
    return arr


def newPart(arr,l,h):
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def newQSort(arr,l,h):
    if l<h:
        p=newPart(arr,l,h)
        newQSort(arr,l,p-1)
        newQSort(arr,p+1,h)
    return arr




if __name__ == '__main__':  
    arr=[10,80,30,90,50,70,100,30]
    print(len(arr)-1)
    print(lomuto_partition(arr,0,len(arr)-1))
    print(sortByLomuto(arr,0,len(arr)-1))
    print(pracQSort(arr,0,len(arr)-1))
    print(newQSort(arr,0,len(arr)-1))