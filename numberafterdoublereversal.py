class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a=str(num)
        b=a[::-1]
        c=int(b)
        d=str(c)
        e=d[::-1]
        f=len(e)
        f=int(e)
        if (num==f):
            return True
        else:
            return False



        