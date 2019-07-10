











class Solution(object):
    def numIslands2(self, m, n, positions):

        island_count = [0]
        parent = {}
        for r, c in positions:
            nbors = set()
            for nbor in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nbor in parent:
                    island = parent[nbor]
                    while island != parent[island]:
                        parent[island] = parent[parent[island]]
                        island = parent[island]
                    nbors.add(island)
            if not nbors:
                parent[(r, c)] = (r, c)
                island_count.append(island_count[-1] + 1)
            else:
                this_island = nbors.pop()
                for nbor in nbors:
                    parent[nbor] = this_island
                parent[(r, c)] = this_island
                island_count.append(island_count[-1] - len(nbors))
        return island_count[1:]
