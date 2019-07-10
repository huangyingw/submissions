














from collections import defaultdict


class Solution(object):
    def smallestEquivalentString(self, A, B, S):

        equivalents = defaultdict(set)
        for a, b in zip(A, B):
            equivalents[a].add(b)
            equivalents[b].add(a)
        minimum = {}

        def get_minimum(char):
            if char in minimum:
                return minimum[char]
            result = char
            visited = set()
            queue = {char}
            while queue:
                c = queue.pop()
                if c in visited:
                    continue
                visited.add(c)
                result = min(result, c)
                queue |= equivalents[c]
            for v in visited:
                minimum[v] = result
            return result
        return "".join(get_minimum(c) for c in S)
