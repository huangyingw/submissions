class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        mapping = dict()
        for i, n in enumerate(nums):
            if n in mapping and i - mapping[n] <= k:
                return True
            else:
                mapping[n] = i
        return False

    def containsNearbyDuplicate(self, nums, k):
        if len(set(nums)) == len(nums):
            return False
        l = len(nums)
        for i in range(l):
            j = 1
            while j <= k and i + j < l:
                if nums[i] == nums[i + j]:
                    return True
                j += 1
        return False
