_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        front, back = 0, len(nums) - 1
        moves = 0
        while front < back:
            moves += nums[back] - nums[front]
            front += 1
            back -= 1
        return moves
