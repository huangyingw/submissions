_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def judgePoint24(self, nums):

        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 0.001
        for i in range(n - 1):
            for j in range(i + 1, n):
                remainder = nums[:i] + nums[i + 1:j] + nums[j + 1:]
                if self.judgePoint24(remainder + [nums[i] + nums[j]]):
                    return True
                if self.judgePoint24(remainder + [nums[i] - nums[j]]):
                    return True
                if self.judgePoint24(remainder + [nums[j] - nums[i]]):
                    return True
                if self.judgePoint24(remainder + [nums[i] * nums[j]]):
                    return True
                if nums[j] != 0 and self.judgePoint24(remainder + [float(nums[i]) / float(nums[j])]):
                    return True
                if nums[i] != 0 and self.judgePoint24(remainder + [float(nums[j]) / float(nums[i])]):
                    return True
        return False
