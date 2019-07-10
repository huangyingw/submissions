_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def addBinary(self, a, b):

        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while carry or i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(result[::-1])
