class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        elif n==1:
            return True
        elif (n>1 and n<4):
            return False
        else:
            while(n%4==0):
                n//=4
            if(n==1):
                return True
            else:
                return False 

        