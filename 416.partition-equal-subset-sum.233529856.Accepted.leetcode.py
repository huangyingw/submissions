class Solution(object):
    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        nums.sort(reverse=True)
        target = sum_nums // 2
        subset_sum = [True] + [False] * target
        for num in nums:
            for i in range(target - 1, -1, -1):
                if subset_sum[i] and i + num <= target:
                    if i + num == target:
                        return True
                    subset_sum[i + num] = True
        return False
from collections import Counter
class Solution2(object):
    def canPartition(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        freq = Counter(nums)
        return self.partition(freq, nums_sum // 2)
    def partition(self, freq, target):
        if target == 0:
            return True
        if target < 0:
            return False
        for num in freq:
            if freq[num] == 0:
                continue
            freq[num] -= 1
            if self.partition(freq, target - num):
                return True
            freq[num] += 1
        return False
