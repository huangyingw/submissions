_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest, next_smallest = float("inf"), float("inf")
        for num in nums:
            smallest = min(smallest, num)
            if num > smallest:
                next_smallest = min(next_smallest, num)
            if num > next_smallest:
                return True
        return False
