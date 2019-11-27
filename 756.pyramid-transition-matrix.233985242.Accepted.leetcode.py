from collections import defaultdict


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        triangles = defaultdict(list)
        for triple in allowed:
            triangles[triple[:-1]].append(triple[-1])

        def helper(prev, current):
            if len(prev) == 1:
                return True
            n = len(current)
            if n == len(prev) - 1:
                return helper(current, "")
            colours = triangles[prev[n:n + 2]]
            if not colours:
                return False
            for colour in colours:
                if helper(prev, current + colour):
                    return True
            return False
        return helper(bottom, "")
