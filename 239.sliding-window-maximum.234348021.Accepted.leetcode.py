from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        ret = []
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret
