_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def smallestFactorization(self, a):

        if a == 1:
            return 1
        result = 0
        tens = 1
        for digit in range(9, 1, -1):
            while a != 1 and a % digit == 0:
                result += digit * tens
                if result > 2 ** 31:
                    return 0
                a //= digit
                if a == 1:
                    return result
                tens *= 10
        return 0
