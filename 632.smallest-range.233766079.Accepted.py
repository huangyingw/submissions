_author_ = 'jake'
_project_ = 'leetcode'








import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        window = [(nums[i][0], 0, i) for i in range(n)]
        heapq.heapify(window)
        heap_min, heap_max = window[0][0], max([nums[i][0] for i in range(n)])
        best_min, best_max = heap_min, heap_max
        while True:
            _, i, i_list = heapq.heappop(window)
            if i + 1 >= len(nums[i_list]):
                return [best_min, best_max]
            heapq.heappush(window, (nums[i_list][i + 1], i + 1, i_list))
            heap_min = window[0][0]
            heap_max = max(heap_max, nums[i_list][i + 1])
            if heap_max - heap_min < best_max - best_min:
                best_min, best_max = heap_min, heap_max
