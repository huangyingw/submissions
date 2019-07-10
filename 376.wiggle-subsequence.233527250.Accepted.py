_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def wiggleMaxLength(self, nums):

        if not nums:
            return 0
        max_length = 1
        prev = nums[0]
        direction = 0
        for num in nums[1:]:
            if direction != -1 and num < prev:
                max_length += 1
                direction = -1
            elif direction != 1 and num > prev:
                max_length += 1
                direction = 1
            prev = num
        return max_length
