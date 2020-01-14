class Solution(object):
    def findNumbers(self, nums):
        return sum(len(str(num)) % 2 == 0 for num in nums)
