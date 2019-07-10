













class Solution(object):
    def minSwapsCouples(self, row):

        n = len(row) // 2
        couple_to_location = [[] for _ in range(n)]
        for i, person in enumerate(row):
            couple_to_location[person // 2].append(i // 2)
        adjacency = [[] for _ in range(n)]
        for a, b in couple_to_location:
            adjacency[a].append(b)
            adjacency[b].append(a)
        swaps = n

        for start in range(n):
            if not adjacency[start]:
                continue
            swaps -= 1
            a = start
            b = adjacency[start].pop()
            while b != start:
                adjacency[b].remove(a)
                a, b = b, adjacency[b].pop()
        return swaps
