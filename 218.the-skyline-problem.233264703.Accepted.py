_author_ = 'jake'
_project_ = 'leetcode'













import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = [(0, 0)]
        current = [(0, float('inf'))]
        edges = [(l, -h, r) for l, r, h in buildings]
        edges += [(r, 0, None) for _, r, _ in buildings]
        edges.sort()
        for x, neg_h, r in edges:
            while current[0][1] <= x:
                heapq.heappop(current)
            if neg_h != 0:
                heapq.heappush(current, (neg_h, r))
            if skyline[-1][1] != -current[0][0]:
                skyline.append([x, -current[0][0]])
        return skyline[1:]
