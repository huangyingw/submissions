from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        after = defaultdict(int)
        order = defaultdict(set)
        seen = set(words[0])
        for i in range(1, len(words)):
            diff_to_prev = False
            for j, c in enumerate(words[i]):
                seen.add(c)
                if j < len(words[i - 1]) and not diff_to_prev and c != words[i - 1][j]:
                    if c not in order[words[i - 1][j]]:
                        order[words[i - 1][j]].add(c)
                        after[c] += 1
                    diff_to_prev = True
            if not diff_to_prev and len(words[i - 1]) > len(words[i]):
                return ""
        for c in seen:
            if c not in after:
                after[c] = 0
        frontier = set()
        for a in after:
            if after[a] == 0:
                frontier.add(a)
        letters = []
        while frontier:
            b = frontier.pop()
            del after[b]
            letters.append(b)
            for a in order[b]:
                after[a] -= 1
                if after[a] == 0:
                    frontier.add(a)
        if after:
            return ""
        return "".join(letters)
