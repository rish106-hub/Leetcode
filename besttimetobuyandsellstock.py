class Solution:
    def maxProfit(self, price):
        buy = price[0]
        prft = 0
        for i in range(1, len(price)):
            if price[i] < buy:
                buy = price[i]
            elif price[i] - buy > prft:
                prft = price[i] - buy
        return prft
        