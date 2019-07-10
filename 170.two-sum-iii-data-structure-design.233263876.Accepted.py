_author_ = 'jake'
_project_ = 'leetcode'











class TwoSum(object):
    def __init__(self):

        self.nums = {}

    def add(self, number):

        self.nums[number] = number in self.nums

    def find(self, value):

        for num in self.nums:
            if value == 2 * num:
                if self.nums[num]:
                    return True
            else:
                if value - num in self.nums:
                    return True
        return False
