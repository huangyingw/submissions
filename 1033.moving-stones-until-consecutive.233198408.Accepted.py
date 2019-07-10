


class Solution(object):
    def numMovesStones(self, a, b, c):
        lista = [a, b, c]
        lista.sort()
        a, b, c = lista[0], lista[1], lista[2]
        minsteps = 0
        if b == a + 1 and c == a + 2:
            return [0, 0]
        elif b == a + 1 or c == b + 1 or c == b + 2 or b == a + 2:
            minsteps = 1
        else:
            minsteps = 2
        return [minsteps, b - a - 1 + c - b - 1]
