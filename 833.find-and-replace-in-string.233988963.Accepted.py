_author_ = 'jake'
_project_ = 'leetcode'



















class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):

        replaced = [c for c in S]
        for i, src, tgt in zip(indexes, sources, targets):
            n = len(src)
            if S[i:i + n] == src:
                replaced[i] = tgt
                replaced[i + 1:i + n] = [""] * (n - 1)
        return "".join(replaced)
