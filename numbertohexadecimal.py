class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = (1 << 32) + num           
        num=hex(num)
        return num[2:]
