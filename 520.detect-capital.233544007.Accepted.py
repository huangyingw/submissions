_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        first = word[0] <= "Z"
        second = word[1] <= "Z"
        if not first and second:
            return False
        for c in word[2:]:
            if (c <= "Z") != second:
                return False
        return True
