class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        begin = 0
        for index in range(len(nums)):
            if index == 0 or nums[index] != nums[index - 1]:
                begin = 0
            size = len(res)
            for j in range(begin, size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
            begin = size
        return res
