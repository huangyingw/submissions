class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i == -1:
            return [1] + digits
        return digits[:i] + [digits[i] + 1] + digits[i + 1:]
