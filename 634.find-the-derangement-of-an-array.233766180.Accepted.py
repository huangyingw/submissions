















class Solution(object):
    def findDerangement(self, n):

        MODULO = 10 ** 9 + 7
        derange, one_correct = 0, 1
        for i in range(2, n + 1):
            derange, one_correct = (derange * (i - 1) + one_correct) % MODULO, (i * derange) % MODULO
        return derange
