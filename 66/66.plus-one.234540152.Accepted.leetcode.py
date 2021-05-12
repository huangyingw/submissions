class Solution:
    def plusOne(self, digits):
        return list(map(int, str(int("".join(map(str, digits))) + 1)))

    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits
