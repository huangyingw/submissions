_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy, sell = float("-inf"), 0
        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)
        return sell
