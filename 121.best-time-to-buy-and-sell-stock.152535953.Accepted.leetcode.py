class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = sys.maxint

        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)

        return maxProfit
