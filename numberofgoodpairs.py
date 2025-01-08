class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        rep={}
        for num in nums:
            if num in rep:
                count+=rep[num]
                rep[num]+=1
            else:
                rep[num]=1
        return count

