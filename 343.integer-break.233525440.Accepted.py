_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def integerBreak(self, n):

        if n <= 3:
            return n - 1
        threes, remainder = divmod(n - 4, 3)
        product = 3**threes
        remainder += 4
        if remainder == 4:
            return product * 2 * 2
        if remainder == 5:
            return product * 3 * 2
        return product * 3 * 3


class Solution2(object):
    def integerBreak(self, n):

        max_breaks = [0, 1]
        for i in range(2, n + 1):
            max_break = 0
            for j in range(1, (i // 2) + 1):

                max_break = max(max_break, max(j, max_breaks[j]) * max(i - j, max_breaks[i - j]))
            max_breaks.append(max_break)
        return max_breaks[-1]
