_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        diff = ord("a") - ord("A")
        return "".join(chr(ord(c) + diff) if "A" <= c <= "Z" else c for c in str)
