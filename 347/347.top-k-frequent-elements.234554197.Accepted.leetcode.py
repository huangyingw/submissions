class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count, key=count.get)
