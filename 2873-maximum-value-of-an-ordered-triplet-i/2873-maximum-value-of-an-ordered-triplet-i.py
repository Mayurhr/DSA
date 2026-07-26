class Solution(object):
    def maximumTripletValue(self, nums):
        ans=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                   value=(nums[i] - nums[j]) * nums[k]
                   ans=max(ans,value)
        return ans
        