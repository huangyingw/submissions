_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) != len(words[0]):
            return False
        n = len(words[0])
        for i, word in enumerate(words[1:], 1):
            m = len(word)
            if m > n:
                return False
            words[i] += (n - m) * " "
        for i in range(n):
            for j in range(n):
                if words[i][j] != words[j][i]:
                    return False
        return True
