class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ct = -1
        while n > 0:
            if n % 2 == ct:
                return False
            ct = n % 2
            n //= 2
        return True
        