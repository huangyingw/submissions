class Solution(object):

    def containsDuplicate(self, nums):

        mapping = dict()
        for i in nums:
            if i in mapping:
                return True
            else:
                mapping[i] = 1
        return False

    def containsDuplicate(self, nums):

        if(len(set(nums)) == len(nums)):
            return False
        return True

    def containsDuplicate(self, nums):

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
