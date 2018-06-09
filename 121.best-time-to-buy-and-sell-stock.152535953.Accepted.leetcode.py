class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = sys.maxint

        for price in prices:
            if price < minPrice:
                minPrice = price

            if (price - minPrice) > maxProfit:
                maxProfit = price - minPrice

        return maxProfit
