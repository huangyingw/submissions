class Solution(object):
    def maxProfit(self, prices):
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(-price, buy)
            sell = max(price + buy, sell)
        return sell
