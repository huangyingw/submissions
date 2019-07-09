_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            copy = num
            while copy > 0:
                copy, digit = divmod(copy, 10)
                if digit == 0 or num % digit != 0:
                    return False
            return True
        return [num for num in range(left, right + 1) if is_self_dividing(num)]
