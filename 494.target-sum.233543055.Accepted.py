_author_ = 'jake'
_project_ = 'leetcode'








from collections import defaultdict


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = defaultdict(int)
        sums[0] = 1
        running = nums[:]
        for i in range(len(nums) - 2, -1, -1):
            running[i] += running[i + 1]
        for i, num in enumerate(nums):
            new_sums = defaultdict(int)
            for old_sum in sums:
                if S <= old_sum + running[i]:
                    new_sums[old_sum + num] += sums[old_sum]
                if S >= old_sum - running[i]:
                    new_sums[old_sum - num] += sums[old_sum]
            sums = new_sums
        if S not in sums:
            return 0
        return sums[S]
