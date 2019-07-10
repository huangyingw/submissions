_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def maxProfit(self, prices):

        return sum([max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices))])
