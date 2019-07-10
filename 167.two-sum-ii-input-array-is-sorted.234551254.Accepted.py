class Solution(object):
    def twoSum(self, numbers, target):
        n = {}
        for index, num in enumerate(numbers):
            temp = target - num
            if temp in n:
                return [n[temp] + 1, index + 1]
            n[num] = index
