_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        substrings, repeated = set(), set()
        TARGET = 10
        for i in range(len(s) - TARGET + 1):
            substring = s[i:i + TARGET]
            if substring in substrings:
                repeated.add(substring)
            else:
                substrings.add(substring)
        return list(repeated)
