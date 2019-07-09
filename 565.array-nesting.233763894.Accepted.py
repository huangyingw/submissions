_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        longest = 0
        for i, num in enumerate(nums):
            if num in visited:
                continue
            current = set()
            while num not in current:
                current.add(num)
                num = nums[num]
            longest = max(longest, len(current))
            if longest >= len(nums) - i - 1:
                break
            visited |= current
        return longest
