class Solution(object):
    def numberOfSubarrays(self, nums, k):
        odds = [-1] + [i for i, num in enumerate(nums) if num % 2 == 1] + [len(nums)]
        result = 0
        for j, end in enumerate(odds[k:-1], k):
            ends = odds[j + 1] - end
            starts = odds[j - k + 1] - odds[j - k]
            result += starts * ends
        return result
