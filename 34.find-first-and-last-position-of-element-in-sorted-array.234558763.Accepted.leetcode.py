class Solution(object):
    def searchRange(self, nums, target):
        leftIndex = self.binarySearch(nums, target, True)
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        return [leftIndex, self.binarySearch(nums, target, False)]

    def binarySearch(self, nums, target, flag):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] > target or (nums[mid] == target and flag):
                high = mid - 1
            else:
                low = mid + 1
        return low if flag else high
