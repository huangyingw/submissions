


class Solution(object):
    def twoSum(self, nums, target):

        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                return [record[nums[i]], i]
            record[target - nums[i]] = i
        return []
