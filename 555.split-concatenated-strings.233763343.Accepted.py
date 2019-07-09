_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = None
        best = [max(s, s[::-1]) for s in strs]
        for i, s in enumerate(strs):
            t = s[::-1]
            for j in range(len(s)):
                test = s[j:] + "".join(best[i + 1:] + best[:i]) + s[:j]
                test2 = t[j:] + "".join(best[i + 1:] + best[:i]) + t[:j]
                result = max(result, test, test2)
        return result
