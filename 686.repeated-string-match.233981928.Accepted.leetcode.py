class Solution(object):
    def repeatedStringMatch(self, A, B):
        if set(B) - set(A):
            return -1
        div, mod = divmod(len(B), len(A))
        if mod != 0:
            div += 1
        for i in range(2):
            if B in A * (div + i):
                return div + i
        return -1
