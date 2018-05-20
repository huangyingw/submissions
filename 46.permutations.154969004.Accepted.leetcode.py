#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (47.53%)
# Total Accepted:    234.6K
# Total Submissions: 493.7K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#
#


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper():
            for index in range(len(nums)):
                if len(current) == len(nums):
                    result.append(list(current))
                    return
                if not visited[index]:
                    visited[index] = True
                    current.append(nums[index])
                    helper()
                    current.pop()
                    visited[index] = False
        visited = [False for _ in range(len(nums))]
        current = []
        result = []
        helper()
        return result
