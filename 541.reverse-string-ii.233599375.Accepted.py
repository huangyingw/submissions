_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        reverse = True
        result = []
        for i in range(0, len(s), k):
            block = s[i:i + k]
            if reverse:
                result.append(block[::-1])
            else:
                result.append(block)
            reverse = not reverse
        return "".join(result)
