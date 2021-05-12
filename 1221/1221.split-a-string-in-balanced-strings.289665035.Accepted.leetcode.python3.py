class Solution(object):
    def balancedStringSplit(self, s):
        balance = 0
        result = 0
        for c in s:
            balance += 1 if c == "L" else -1
            if balance == 0:
                result += 1
        return result
