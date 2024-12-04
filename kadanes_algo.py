from sys import maxsize

def maxSumSubArray(arr):
    size=len(arr)
    currSum=0
    maxSoFar =  arr[0]
    for i in range(size):
        currSum += arr[i]
        if currSum > maxSoFar:
            maxSoFar = currSum
        if currSum<0:
            currSum = 0
    return maxSoFar


def maxSubArraySumWithIndex(arr):
    maxSoFar = -maxsize-1
    maxEndingHere = 0
    start,end,s=0,0,0
    size = len(arr)
    
    for i in range(0,size):
        maxEndingHere += arr[i]
        if maxSoFar < maxEndingHere :
            maxSoFar = maxEndingHere
            start =s
            end = i
        
        if maxEndingHere < 0:
            maxEndingHere = 0
            s=i+1
    
    return f"{maxSoFar} is the maximum sum of subarray which starts at {start} and ends at {end}."

def maxSumArrayByDP(arr):
    size = len(arr)
    dp = [0]*size
    dp[0]=arr[0]
    ans = dp[0]
    for i in range(1,size):
        dp[i]=max(arr[i],dp[i-1]+arr[i])
        
        ans = max(ans,dp[i])
    return ans

def lonngestConsecutiveSeq(nums):
    nums = set(nums)
    best = 0

    for i in nums:
        if i-1 not in nums:
            j = i+1
            while j in nums:
                j+=1
                best=max(best,j-i)
        return best


if __name__ == '__main__':
    
    arr = [-2,-3,4,-1,-2,1,5,-3]
    newArr = [1,3,5,4,2,22,43,23,24]
    print(maxSumSubArray(arr))
    print(maxSubArraySumWithIndex(arr))
    print(maxSumArrayByDP(arr))
    print(lonngestConsecutiveSeq(newArr))
    