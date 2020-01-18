class Solution(object):
    def maxProfit(self, prices, fee):
        buy, sell = float("-inf"), 0
        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)
        return sell
