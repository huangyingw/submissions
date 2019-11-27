class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        result = (C - A) * (D - B) + (G - E) * (H - F)
        if (C <= E or G <= A or H <= B or D <= F):
            return result
        dx = min(C, G) - max(A, E)
        dy = min(D, H) - max(B, F)
        return result - dx * dy
