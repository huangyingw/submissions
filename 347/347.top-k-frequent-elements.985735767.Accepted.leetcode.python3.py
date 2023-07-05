import heapq


class Solution:
    def topKFrequent(self, nums, k):

        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        heap = []
        for num, freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heappushpop(heap, (freq, num))
        return [item[1] for item in heap]
