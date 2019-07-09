_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.append(float("inf"))
        prev = nums[0]
        for num in nums[1:]:
            missing = num - prev - 1
            if k - missing <= 0:
                return prev + k
            k -= missing
            prev = num
