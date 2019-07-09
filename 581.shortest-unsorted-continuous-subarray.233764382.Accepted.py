_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        right, left = -1, -1
        for i in range(1, n):
            if left == - 1 and nums[i] < nums[i - 1]:
                left = i - 1
                min_num = nums[i]
            elif left != -1:
                min_num = min(min_num, nums[i])
        if left == -1:
            return 0
        for i in range(n - 2, -1, -1):
            if right == -1 and nums[i] > nums[i + 1]:
                right = i + 1
                max_num = nums[i]
            elif right != -1:
                max_num = max(max_num, nums[i])
        while left > 0 and nums[left - 1] > min_num:
            left -= 1
        while right < n - 1 and nums[right + 1] < max_num:
            right += 1
        return right - left + 1
