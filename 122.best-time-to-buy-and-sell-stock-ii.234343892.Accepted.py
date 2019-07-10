class Solution:
    def maxProfit(self, prices):

        buy, sell = float('-inf'), 0
        for i in range(len(prices)):
            buy, sell = max(buy, sell - prices[i]), max(sell, buy + prices[i])
        return sell
