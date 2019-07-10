



class Solution:
    def smallestRange(self, A):
        import functools
        A = [row[::-1] for row in A]
        ans = -1e9, 1e9
        for left in sorted(functools.reduce(set.union, map(set, A))):
            right = -1e9
            for B in A:
                while B and B[-1] < left:
                    B.pop()
                if not B:
                    return ans
                right = max(right, B[-1])
            if right - left < ans[1] - ans[0]:
                ans = left, right
        return ans
import heapq


class Solution:
    def smallestRange(self, nums):

        queue = [(list_num[0], i, 0) for i, list_num in enumerate(nums)]
        heapq.heapify(queue)
        result = [float("-inf"), float("inf")]
        right = max(row[0] for row in nums)
        while queue:
            left, i, j = heapq.heappop(queue)
            if right - left < result[1] - result[0]:
                result = [left, right]
            if j == len(nums[i]) - 1:
                return result
            next_num_val = nums[i][j + 1]
            right = max(right, next_num_val)
            heapq.heappush(queue, (next_num_val, i, j + 1))
