


class Solution(object):
    def rotateString(self, A, B):

        if len(A) != len(B):
            return False
        c = A + A
        return B in c
