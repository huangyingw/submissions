_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        if not nuts:
            return 0
        nuts_to_tree = 0
        best_gain = height * width

        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        for nut in nuts:
            nut_to_tree = distance(nut, tree)
            squirrel_to_nut = distance(squirrel, nut)
            nuts_to_tree += nut_to_tree
            best_gain = min(best_gain, squirrel_to_nut - nut_to_tree)
        return 2 * nuts_to_tree + best_gain
