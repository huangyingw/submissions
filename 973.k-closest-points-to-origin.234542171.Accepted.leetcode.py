class Solution:
    def kClosest(self, points, K):
        import heapq
        return heapq.nsmallest(K, points, key=lambda p: p[0]**2 + p[1]**2)
