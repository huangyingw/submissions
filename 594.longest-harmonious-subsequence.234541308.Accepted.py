class Solution:
    def findLHS(self, nums):
        from collections import Counter
        res = 0
        mapping = Counter(nums)
        for k in mapping.keys():
            if k + 1 in mapping:
                res = max(res, mapping.get(k) + mapping.get(k + 1))
        return res
