class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        start, end, max_index = 0, 0, 0
        steps = 1
        while True:
            for i in range(start, end):
                max_index = max(max_index, i + nums[i])
            if max_index >= len(nums) - 1:
                return steps
            steps += 1
            start, end = end + 1, max_index
