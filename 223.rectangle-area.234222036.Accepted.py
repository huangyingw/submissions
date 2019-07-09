class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        result = (C - A) * (D - B) + (G - E) * (H - F)

        if (C <= E or G <= A or H <= B or D <= F):
            return result

        dx = min(C, G) - max(A, E)

        dy = min(D, H) - max(B, F)
        return result - dx * dy
