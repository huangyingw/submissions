


class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        mini = min(A)
        result = 0
        while mini > 0:
            quo = mini % 10
            rem = mini / 10
            result += quo
            mini = rem
        return 0 if result % 2 else 1
