_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def circularArrayLoop(self, nums):

        n = len(nums)
        for i, num in enumerate(nums):
            pos = num > 0
            j = (i + num) % n
            steps = 1
            while steps < n and nums[j] % n != 0 and (nums[j] > 0) == pos:
                j = (j + nums[j]) % n
                steps += 1
            if steps == n:
                return True
            nums[i] = 0
            j = (i + num) % n
            while nums[j] % n != 0 and (nums[j] > 0) == pos:
                j, nums[j] = (j + nums[j]) % n, 0
        return False
