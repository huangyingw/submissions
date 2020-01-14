class Solution(object):
    def combinationSum4(self, nums, target):
        memo = {}
        self.helper(nums, target, memo)
        return memo[target]
    def helper(self, nums, target, memo):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if target in memo:
            return memo[target]
        combos = 0
        for num in nums:
            combos += self.helper(nums, target - num, memo)
        memo[target] = combos
        return combos
class Solution2(object):
    def combinationSum4(self, nums, target):
        combos = [0] * (target + 1)
        combos[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    combos[i] += combos[i - num]
        return combos[-1]
