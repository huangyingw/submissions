class Solution(object):
    def sequentialDigits(self, low, high):
        nums = list(range(1, 10))
        result = []
        while nums:
            new_nums = []
            for num in nums:
                if num > high:
                    break
                if num >= low:
                    result.append(num)
                last_digit = num % 10
                if last_digit != 9:
                    new_nums.append(num * 10 + last_digit + 1)
            nums = new_nums
        return result
