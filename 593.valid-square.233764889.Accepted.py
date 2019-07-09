_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def square_dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        points = [p1, p2, p3, p4]
        square_dists = [square_dist(points[i], points[j]) for i in range(4) for j in range(i + 1, 4)]
        side = min(square_dists)
        if max(square_dists) != 2 * side:
            return False
        return square_dists.count(side) == 2 * square_dists.count(2 * side)
