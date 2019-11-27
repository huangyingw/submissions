class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        for index, num in enumerate(nums):
            if num > 0:
                result.append(index + 1)
        return result
