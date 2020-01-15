from collections import Counter


class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        return max(Counter(nums).values()) <= len(nums) // K
