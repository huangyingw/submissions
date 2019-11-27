class Solution(object):
    def findDuplicates(self, nums):
        result = []
        dup = {}
        for i in nums:
            if i in dup:
                result.append(i)
            else:
                dup[i] = 1
        return result
