l=[0]*999
def insert(x):
    l[x]=1
    return "Inserted ",x

def delete(x):
    if l[x]==1:
        l[x]=0
        return "Deleted ",x," Successfully"
    else:
        return "ELement not found" 

def search(x):
    if l[x]==1:
        return True
    else:
        return False
    
print(insert(24))
print(search(24))