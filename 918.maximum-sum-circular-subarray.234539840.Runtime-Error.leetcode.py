'''
53.Maximum Subarray 
# https://leetcode.com/problems/maximum-subarray/description/
这道题的关键是怎样解决圈的问题
对于53题
    # class Solution:
    #     def maxSubArray(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         策略：遍历所有数，如果当前和小于0，则从下一个数开始重新算
    #         用res保存当前最大，current_sum保存遍历数组的和大小
    #         """
    #         res = nums[0] 
    #         current_sum = nums[0]
    #         for i in range(1,len(nums)):
    #             current_sum = max(current_sum + nums[i], nums[i])
    #             res = max(res, current_sum)
    #         return res
此题可以分为两种情况：
1：最大子序列不过端点，等同于53题的情况
2：最大子序列需要过端点，等同于在序列中先找到最小子序列，然后用总和减去最小子序列
max(the max subarray sum, the total sum - the min subarray sum)
'''


def maxSubarraySumCircular(self, A):
    total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
    for a in A:
        curMax = max(curMax + a, a)
        maxSum = max(maxSum, curMax)
        curMin = min(curMin + a, a)
        minSum = min(minSum, curMin)
        total += a
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum
