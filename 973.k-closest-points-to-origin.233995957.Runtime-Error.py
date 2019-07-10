_author_ = 'jake'
_project_ = 'leetcode'







import heapq


class Solution:
    def kClosest(self, points, K):

        return heapq.nsmallest(K, points, lambda x, y: x * x + y * y)
