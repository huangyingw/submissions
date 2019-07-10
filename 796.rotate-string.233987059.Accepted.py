










class Solution(object):
    def rotateString(self, A, B):

        if len(A) != len(B):
            return False
        return A in B + B
