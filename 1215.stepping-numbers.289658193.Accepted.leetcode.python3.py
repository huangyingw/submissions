class Solution(object):
    def countSteppingNumbers(self, low, high):
        result = []
        if low == 0:
            result.append(0)
        nums = [i for i in range(1, 10)]
        while nums:
            new_nums = []
            for num in nums:
                if num > high:
                    continue
                if num >= low:
                    result.append(num)
                last_digit = num % 10
                if last_digit != 0:
                    new_nums.append(num * 10 + last_digit - 1)
                if last_digit != 9:
                    new_nums.append(num * 10 + last_digit + 1)
            nums = new_nums
        return result
