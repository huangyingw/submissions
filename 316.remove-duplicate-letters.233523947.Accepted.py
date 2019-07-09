_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set = sorted(set(s))
        for c in s_set:
            suffix = s[s.index(c):]
            if len(set(suffix)) == len(s_set):
                return c + self.removeDuplicateLetters(suffix.replace(c, ""))
        return ""
