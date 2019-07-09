_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        used = [False] * len(nums)
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        def dfs(subsets, last, partial):
            if subsets == 1:
                return True
            if partial == target:
                return dfs(subsets - 1, 0, 0)
            for i in range(last, len(nums)):
                if not used[i] and partial + nums[i] <= target:
                    used[i] = True
                    if dfs(subsets, i + 1, partial + nums[i]):
                        return True
                    used[i] = False
            return False
        return dfs(k, 0, 0)


class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        nums.sort(reverse=True)
        target = total // k
        if total % k != 0 or nums[0] > target:
            return False
        partition = [0 for _ in range(k)]

        def helper(i):
            if i == len(nums):
                return True
            for j in range(len(partition)):
                if partition[j] + nums[i] <= target:
                    partition[j] += nums[i]
                    if helper(i + 1):
                        return True
                    partition[j] -= nums[i]
                if partition[j] == 0:
                    break
            return False
        return helper(0)
