def naiveApproach(str):                     #   O(n^3)
    n=len(str)
    res = 0
    for i in range(n):
        for j in range(i,n):
            if areDistinct(str,i,j):
                res = max(res,j-i+1)
                
    return res


def areDistinct(str,i,j):
    visited = [0]*256
    for k in range(i,j+1):
        if visited[ord(str[k])]==True:
            return False
        visited[ord(str[k])]=True
    return True


def longestDistinctbetter(str):             #   O(n^2)
    n = len(str)
    print(n)
    res = 0
    for i in range (n):
        visited = [0]*256
        for j in range(i,n):
            if visited[ord(str[j])]:
                break
            else:
                res = max(res,j-i+1)
                visited[ord(str[j])]=1                   
    return res


def longestDistinctstrBest(str):            #   O(n)
    n = len(str)
    res = 0
    prev = [-1]*256
    i=0
    for j in range(n):
        i = max(i,prev[ord(str[j])]+1)
        maxEnd = j-i+1
        res = max(res,maxEnd)
        prev[ord(str[j])]=j
    return j


def isPalin(s):
    left = 0
    right = len(s)-1
    while left <= right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True
 
def isPlindromeNormal(str):
    pal = ''
    str=str.lower()
    for i in str:
        pal = i + pal
    return pal==str



if __name__ =='__main__':
    print(naiveApproach("ababcda"))
    print(longestDistinctbetter("aaaqwertyuiop"))
    print(naiveApproach("aaaqwertyuiop"))
    print(isPalin("malayalam"))
    print(isPlindromeNormal("Naan"))