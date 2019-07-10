_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findSubstringInWraproundString(self, p):

        substring_ending = [0] * 26
        length = 0
        for i, c in enumerate(p):
            if i != 0 and (ord(c) == ord(p[i - 1]) + 1 or ord(c) == ord(p[i - 1]) - 25):
                length += 1
            else:
                length = 1
            substring_ending[ord(c) - ord("a")] = max(substring_ending[ord(c) - ord("a")], length)
        return sum(substring_ending)
