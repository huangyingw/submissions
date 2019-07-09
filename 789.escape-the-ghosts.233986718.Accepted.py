_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def manhattan(position):
            return abs(position[0] - target[0]) + abs(position[1] - target[1])
        target_distance = manhattan((0, 0))
        return all(manhattan(ghost) > target_distance for ghost in ghosts)
