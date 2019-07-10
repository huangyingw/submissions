class Solution:
    def plusOne(self, digits):

        for i in range(len(digits)):
            digits[~i] += 1
            if digits[~i] < 10:
                return digits
            else:
                digits[~i] %= 10
        if digits[0] == 0:
            return [1] + digits
        return digits
