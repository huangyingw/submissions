class Solution:
    def topKFrequent(self, nums, k):

        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        topk = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(topk) < k:
                    topk.append(num)
                else:
                    return topk
        return topk
