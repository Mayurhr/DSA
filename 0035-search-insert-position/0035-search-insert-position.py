class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            k=nums.append(target)
            k==None
            M=sorted(nums)
            Index=M.index(target)
            return Index
        else:
            Index=nums.index(target)
            return Index