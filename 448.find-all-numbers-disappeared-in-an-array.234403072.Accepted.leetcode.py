class Solution:
    def findDisappearedNumbers(self, nums):
        length = len(nums)
        num_set = set(nums)
        res = []
        for i in range(1, length + 1):
            if i not in num_set:
                res.append(i)
        return res

    def findDisappearedNumbers2(self, nums):
        all_nums = [i for i in range(1, len(nums) + 1)]
        return list(set(all_nums) - set(nums))
