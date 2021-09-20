class Solution(object):
    def maxSubArray(self, nums):
        localmax=0
        globalmax=float('-inf')
        
        for num in nums:
            localmax+=num
            if(localmax<num):
                localmax=num
            if(globalmax<localmax):
                globalmax=localmax
        
        return globalmax