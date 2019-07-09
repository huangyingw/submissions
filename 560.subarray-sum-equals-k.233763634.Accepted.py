_author_ = 'jake'
_project_ = 'leetcode'







from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        sums = defaultdict(int)
        running_sum = 0
        for num in nums:
            running_sum += num
            if running_sum == k:
                total += 1
            if running_sum - k in sums:
                total += sums[running_sum - k]
            sums[running_sum] += 1
        return total
