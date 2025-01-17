class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0  
        ctr = 0  
        for mv in nums:
            pos += mv  
            if pos == 0:  
                ctr += 1
        return ctr
