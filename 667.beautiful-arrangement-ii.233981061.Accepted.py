_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def constructArray(self, n, k):

        result = []
        low, high = 1, k + 1
        next_low = True
        while low <= high:
            if next_low:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
            next_low = not next_low
        return result + list(range(k + 2, n + 1))
