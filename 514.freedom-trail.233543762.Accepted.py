_author_ = 'jake'
_project_ = 'leetcode'




















from collections import defaultdict


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))
        char_to_ring = defaultdict(list)
        for i, c in enumerate(ring):
            char_to_ring[c].append(i)
        i_to_steps = {0: 0}
        for k in key:
            new_i_to_steps = {}
            new_indices = char_to_ring[k]
            for new_i in new_indices:
                min_steps = float("inf")
                for i in i_to_steps:
                    min_steps = min(min_steps, i_to_steps[i] + dist(i, new_i))
                new_i_to_steps[new_i] = min_steps
            i_to_steps = new_i_to_steps
        return min(i_to_steps.values()) + len(key)
