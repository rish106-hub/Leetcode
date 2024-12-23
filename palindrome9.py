class Solution:
    def isPalindrome(self, x):
        b = 0
        c = x
        if x < 0:  
            return False
        while x > 0:
            a = x % 10
            b = (b * 10) + a
            x = x // 10
        return c == b
