class Solution:
    def arrayNesting(self, nums):
        res = 0
        for i in range(len(nums)):
            if nums[i] != -1:
                start = nums[i]
                count = 0
                while nums[start] != -1:
                    temp = start
                    start = nums[start]
                    nums[temp] = -1
                    count += 1
                res = max(count, res)
        return res
