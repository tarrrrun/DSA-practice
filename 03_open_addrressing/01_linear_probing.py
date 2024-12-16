class myHash:
    def __init__(self,b):
        self.bucket=b
        self.table=[None]*b

    def insert(self,x):
        i=x%self.bucket
        if self.table[i]==None:
            self.table[i]=x
        else:
            while self.table[i]!=None:
                if i==self.bucket:
                    break
                i+=1
            if i==self.bucket:
                return ""

