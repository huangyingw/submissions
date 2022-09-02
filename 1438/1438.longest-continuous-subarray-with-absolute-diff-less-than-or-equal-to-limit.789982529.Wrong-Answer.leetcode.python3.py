class Solution(object):
    def longestSubarray(self, nums, limit):
        q_max = q_min = []
        ans = end = begin = 0
        while end < len(nums):
            while q_min and nums[end] < q_min[-1]:
                q_min.pop()
            q_min.append(nums[end])
            while q_max and nums[end] > q_max[-1]:
                q_max.pop()
            q_max.append(nums[end])
            while q_max[0] - q_min[0] > limit:
                if q_min[0] == nums[begin]:
                    q_min.pop(0)
                if q_max[0] == nums[begin]:
                    q_max.pop(0)
                begin += 1
            ans = max(ans, end - begin + 1)
            end += 1
        return ans
