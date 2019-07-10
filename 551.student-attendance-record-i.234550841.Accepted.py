class Solution(object):
    def checkRecord(self, s):
        L = A = 0
        for c in s:
            if c == 'L':
                L += 1
            else:
                L = 0
                if c == 'A':
                    A += 1
            if L > 2 or A > 1:
                return False
        return True
