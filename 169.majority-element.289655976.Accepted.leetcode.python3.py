class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = ans = 0
        for n in nums:
            if count == 0:
                ans = n
            count += 1 if ans == n else -1
        return ans
