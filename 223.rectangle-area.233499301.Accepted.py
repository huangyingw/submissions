class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        x_lhs = max(A, E)
        x_rhs = min(C, G)
        x_overlap = max(x_rhs - x_lhs, 0)
        y_lhs = max(B, F)
        y_rhs = min(D, H)
        y_overlap = max(y_rhs - y_lhs, 0)
        rect1 = (C - A) * (D - B)
        rect2 = (G - E) * (H - F)
        return rect1 + rect2 - y_overlap * x_overlap
