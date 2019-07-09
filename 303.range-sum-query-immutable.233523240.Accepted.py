_author_ = 'jake'
_project_ = 'leetcode'







class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumul = [0]
        for num in nums:
            self.cumul.append(self.cumul[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumul[j + 1] - self.cumul[i]
