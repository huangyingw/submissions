_author_ = 'jake'
_project_ = 'leetcode'
















from collections import defaultdict


class Solution(object):
    def numSimilarGroups(self, A):

        N, W = len(A), len(A[0])
        word_swap = defaultdict(set)
        if N < 2 * W:
            for i, w1 in enumerate(A):
                for j in range(i + 1, len(A)):
                    w2 = A[j]
                    if len([True for c1, c2 in zip(w1, w2) if ord(c1) - ord(c2) != 0]) == 2:
                        word_swap[w1].add(w2)
                        word_swap[w2].add(w1)
        else:
            A_set = set(A)

        def get_neighbours(a):
            if word_swap:
                return word_swap[a]
            neighbours = set()
            for i in range(W - 1):
                for j in range(i + 1, W):
                    if a[i] != a[j]:
                        neighbour = a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
                        if neighbour in A_set:
                            neighbours.add(neighbour)
            return neighbours
        groups = 0
        visited = set()

        def dfs(w):
            visited.add(w)
            for nbor in get_neighbours(w):
                if nbor not in visited:
                    dfs(nbor)
        for word in A:
            if word in visited:
                continue
            groups += 1
            dfs(word)
        return groups
