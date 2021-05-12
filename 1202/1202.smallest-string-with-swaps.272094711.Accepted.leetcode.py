from collections import defaultdict


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        parents = {i: i for i in range(n)}

        def find(i):
            while parents[i] != i:
                parents[i] = parents[parents[i]]
                i = parents[i]
            return i
        for a, b in pairs:
            parents[find(a)] = find(b)
        parent_to_children = defaultdict(list)
        for i in range(n):
            parent_to_children[find(i)].append(i)
        result = [None] * n
        for children in parent_to_children.values():
            chars = sorted(s[i] for i in children)
            for child, char in zip(children, chars):
                result[child] = char
        return "".join(result)
