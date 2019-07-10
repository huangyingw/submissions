









class Solution(object):
    def twoSum(self, numbers, target):

        left, right = 0, len(numbers) - 1
        while True:
            pair_sum = numbers[left] + numbers[right]
            if pair_sum == target:
                return [left + 1, right + 1]
            if pair_sum < target:
                left += 1
            else:
                right -= 1
