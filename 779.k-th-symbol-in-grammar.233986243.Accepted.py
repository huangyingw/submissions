










class Solution(object):
    def kthGrammar(self, N, K):

        length = 2 ** (N - 1)
        inverse = False
        while length > 1:
            if K > length // 2:
                inverse = not inverse
                K -= length // 2
            length //= 2
        return int(inverse)
