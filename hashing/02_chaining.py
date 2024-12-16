class myHash:
    def __init__(self,b):
        self.bucket=b
        self.table=[[] for i in range (b)]

    def insert(self,x):
        i=x%self.bucket
        self.table[i].append(x)
        return "added"

    def remove(self,x):
        i=x%self.bucket
        if x in self.table[i]:
            self.table[i].remove(x)
        else:
            return "NOT FOUND"
        
    def search(self,x):
        i=x%self.bucket
        return x in self.table[i]
    
b = myHash(7)
print(b.insert(71))
print(b.search(71))
print(b.insert(70))
print(b.insert(56))
print(b.table)
print(b.remove(56))
print(b.table)


