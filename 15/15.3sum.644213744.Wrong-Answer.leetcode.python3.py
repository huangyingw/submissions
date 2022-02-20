class Solution(object):
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k + 1 < len(nums) and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result += [[nums[i], nums[j], nums[k]]]
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return result
