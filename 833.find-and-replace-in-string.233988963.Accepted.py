_author_ = 'jake'
_project_ = 'leetcode'



















class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        replaced = [c for c in S]
        for i, src, tgt in zip(indexes, sources, targets):
            n = len(src)
            if S[i:i + n] == src:
                replaced[i] = tgt
                replaced[i + 1:i + n] = [""] * (n - 1)
        return "".join(replaced)
