_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        negative = num < 0
        num = abs(num)
        base_7 = []
        while num:
            num, digit = divmod(num, 7)
            base_7.append(str(digit))
        if negative:
            base_7.append("-")
        return "".join(base_7[::-1]) or "0"
