_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, prev_sell = float("-inf"), 0, 0
        for i, price in enumerate(prices):
            buy = max(buy, prev_sell - price)
            prev_sell = sell
            sell = max(sell, buy + price)
        return sell
