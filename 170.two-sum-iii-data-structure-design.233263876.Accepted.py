_author_ = 'jake'
_project_ = 'leetcode'











class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.nums[number] = number in self.nums

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            if value == 2 * num:
                if self.nums[num]:
                    return True
            else:
                if value - num in self.nums:
                    return True
        return False
