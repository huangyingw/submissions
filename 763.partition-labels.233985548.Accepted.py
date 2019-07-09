_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        result = []
        start, end = 0, 0
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
