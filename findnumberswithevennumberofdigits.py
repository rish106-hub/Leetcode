class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=""
        b=0
        c=0
        for num in nums:
            a=str(num)
            if (len(a)%2==0):
                b=int(a)
                c+=1
        return c