_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        specials = []
        if not S:
            return ""
        balance, start = 0, 0
        for i, c in enumerate(S):
            balance += 1 if c == "1" else -1
            if balance == 0:
                specials.append("1" + self.makeLargestSpecial(S[start + 1:i]) + "0")
                start = i + 1
        specials.sort(reverse=True)
        return "".join(specials)
