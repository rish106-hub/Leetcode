class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n<1:
            return False
        elif n==2:
            return True
        else:
            while n % 2 == 0:
                n = n // 2
        if n == 1:
            return True
        else:
            return False