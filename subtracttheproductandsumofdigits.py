class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=str(n)
        b=len(a)
        c=1
        d=0
        e=0
        for i in range(b):
            c*=int(a[i])
            d+=int(a[i])
            e=(c-d)
        return(e)
        print(c)
