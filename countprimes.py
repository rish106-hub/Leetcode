class Solution:
    def countPrimes(self, n: int) -> int:
        s, a = [0] * n, 0
        for num in range(2, n):
            if s[num]: continue
            a += 1
            s[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        return a