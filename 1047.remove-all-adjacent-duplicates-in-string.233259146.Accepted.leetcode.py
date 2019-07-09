_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for c in S:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)
        return "".join(result)
