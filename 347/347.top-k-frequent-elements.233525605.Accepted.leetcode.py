from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        frequencies = [[] for _ in range(n + 1)]
        for num, freq in Counter(nums).items():
            frequencies[freq].append(num)
        top_k = []
        while k:
            while not frequencies[n]:
                n -= 1
            top_k.append(frequencies[n].pop())
            k -= 1
        return top_k
