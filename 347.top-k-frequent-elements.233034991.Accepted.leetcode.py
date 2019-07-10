class Solution(object):
    def topKFrequent(self, nums, k):

        counter = collections.Counter(nums)
        return [k for k, v in counter.most_common(k)]
