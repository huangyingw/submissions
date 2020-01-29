class Solution(object):
    def splitArray(self, nums, m):
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) / 2
            if self.can_split(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def can_split(self, nums, m, max_subarray):
        subarray_sum = 0
        for num in nums:
            if num + subarray_sum > max_subarray:
                m -= 1
                if m <= 0:
                    return False
                subarray_sum = num
            else:
                subarray_sum += num
        return True
