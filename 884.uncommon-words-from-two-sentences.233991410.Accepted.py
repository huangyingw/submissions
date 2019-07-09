_author_ = 'jake'
_project_ = 'leetcode'








from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counts = Counter(A.split(" ")) + Counter(B.split(" "))
        return [word for word, count in counts.items() if count == 1]
