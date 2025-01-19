class Solution(object):
    def subarraySum(self, nums):
        tot = 0
        for i in range(len(nums)):
            st = max(0, i - nums[i])
            tot += sum(nums[st:i+1])
        return tot