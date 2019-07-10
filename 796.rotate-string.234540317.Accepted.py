



class Solution:
    def rotateString(self, A, B):

        if len(B) != len(A):
            return False
        return B in A + A
