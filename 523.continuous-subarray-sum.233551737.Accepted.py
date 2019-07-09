_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_sum, prefix_sums = 0, {0: -1}
        for i, n in enumerate(nums):
            prefix_sum += n
            if k != 0:
                prefix_sum = prefix_sum % k
            if prefix_sum in prefix_sums:
                if i - prefix_sums[prefix_sum] > 1:
                    return True
            else:
                prefix_sums[prefix_sum] = i
        return False
