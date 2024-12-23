class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)
        r = int(str(x)[::-1])
        if is_negative:
            r = -r
        if ((r < -2**31) or (r > 2**31 - 1)):
            return 0
        return r