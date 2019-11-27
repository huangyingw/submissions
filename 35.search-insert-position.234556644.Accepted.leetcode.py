class Solution:
    def binarysearch(self, nums, target):
        first = 0
        last = len(nums) - 1
        middle = int((first + last) / 2)
        while first <= last:
            if nums[middle] < target:
                first = middle + 1
            elif nums[middle] == target:
                return middle
            else:
                last = middle - 1
            middle = int((first + last) / 2)
            if first > last:
                return first

    def searchInsert(self, nums, target):
        p = self.binarysearch(nums, target)
        return p
