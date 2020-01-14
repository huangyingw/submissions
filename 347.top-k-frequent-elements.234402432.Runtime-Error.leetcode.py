from collections import Counter
class Solution:
    def topKFrequent1(self, nums, k):
        return [v for v, c in Counter(nums).most_common(k)]
    def topKFrequent2(self, nums, k):
        import heapq
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        lst = []
        for e in m:
            heapq.heappush(lst, (-m[e], e))
        res = []
        for i in range(k):
            res.append(heapq.heappop(lst)[1])
        return res
if __name__ == '__main__':
    t = Solution()
