class NumArray(object):
    def __init__(self, nums):
        self.cumul = [0]
        for num in nums:
            self.cumul.append(self.cumul[-1] + num)

    def sumRange(self, i, j):
        return self.cumul[j + 1] - self.cumul[i]
