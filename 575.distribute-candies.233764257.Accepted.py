_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def distributeCandies(self, candies):

        return min(len(candies) // 2, len(set(candies)))
