class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def le_threshold(divisor):
            return sum((num + divisor - 1) // divisor for num in nums) <= threshold
        low, high = 1, max(nums)
        while low < high:
            guess = (low + high) // 2
            if le_threshold(guess):
                high = guess
            else:
                low = guess + 1
        return low
