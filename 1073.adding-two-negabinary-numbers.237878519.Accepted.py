_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def addNegabinary(self, arr1, arr2):

        carry, next_carry = 0, 0
        result = []
        while arr1 or arr2 or carry or next_carry:
            digit = carry
            if arr1:
                digit += arr1.pop()
            if arr2:
                digit += arr2.pop()
            carry, next_carry = next_carry, 0
            result.append(digit % 2)
            if digit == 2 or digit == 3:
                carry += 1
            if digit >= 2:
                if carry >= 2:
                    carry -= 2
                else:
                    next_carry += 1
        while result[-1] == 0 and len(result) > 1:
            result.pop()
        return result[::-1]
