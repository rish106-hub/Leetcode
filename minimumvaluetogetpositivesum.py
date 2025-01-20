class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n=len(nums)
        prefixSum=[0]*n
        prefixSum[0]=nums[0]
        for i in range(1,n):
            prefixSum[i]=prefixSum[i-1]+nums[i]
        minm = min(prefixSum)
        if minm >= 0:
            return 1
        else:
            return 1 - minm