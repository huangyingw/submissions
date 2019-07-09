_author_ = 'jake'
_project_ = 'leetcode'












from collections import defaultdict


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = defaultdict(int)
        for row in wall:
            edge = 0
            for brick in row:
                edge += brick
                edges[edge] += 1
        del edges[sum(wall[0])]
        crossed = len(wall)
        return crossed if not edges else crossed - max(edges.values())
