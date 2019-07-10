













class Solution(object):
    def search(self, nums, target):

        return self.binary(nums, 0, len(nums) - 1, target)

    def binary(self, nums, left, right, target):
        if left > right:
            return False
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[left] < nums[mid]:
            if target < nums[mid] and target >= nums[left]:
                return self.binary(nums, left, mid - 1, target)
            return self.binary(nums, mid + 1, right, target)
        if nums[mid] < nums[right]:
            if target > nums[mid] and target <= nums[right]:
                return self.binary(nums, mid + 1, right, target)
            return self.binary(nums, left, mid - 1, target)
        if nums[left] == nums[mid] and nums[mid] != nums[right]:
            return self.binary(nums, mid + 1, right, target)
        if nums[right] == nums[mid] and nums[mid] != nums[left]:
            return self.binary(nums, left, mid - 1, target)
        if self.binary(nums, left, mid - 1, target):
            return True
        return self.binary(nums, mid + 1, right, target)
