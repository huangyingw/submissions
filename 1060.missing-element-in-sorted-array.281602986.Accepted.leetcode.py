class Solution:
    def missingElement(self, nums, k):
        mis = self.missing(nums, len(nums) - 1)
        if mis < k:
            return nums[-1] + (k - mis)
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            mis = self.missing(nums, mid)
            if mis < k:
                start = mid + 1
            else:
                end = mid
        return nums[start - 1] + (k - self.missing(nums, start - 1))

    def missing(self, nums, index):
        return nums[index] - (nums[0] + index)


class solution:
    def missingElement(self, nums, k):
        index = 0
        for i in range(nums[0], nums[-1] + 1):
            if nums[index] == i:
                index += 1
            else:
                k -= 1
            if k == 0:
                return i
        while k:
            i += 1
            k -= 1
        return i
