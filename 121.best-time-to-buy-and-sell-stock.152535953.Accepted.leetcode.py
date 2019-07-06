class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = sys.maxint
        for price in prices:
            maxProfit = max(price - minPrice, maxProfit)
            minPrice = min(price, minPrice)
        return maxProfit
