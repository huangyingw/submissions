_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findLongestWord(self, s, d):

        def is_subsequence(s, t):
            i, j = 0, 0
            while i < len(s) and (len(t) - j) >= (len(s) - i):
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i == len(s):
                return True
            return False
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            if is_subsequence(word, s):
                return word
        return ""
