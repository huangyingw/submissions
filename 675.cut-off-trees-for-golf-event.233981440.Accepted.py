_author_ = 'jake'
_project_ = 'leetcode'



















class Solution(object):
    def cutOffTree(self, forest):
        rows, cols = len(forest), len(forest[0])
        trees = sorted((h, r, c) for r, row in enumerate(forest)
                       for c, h in enumerate(row) if h > 1)
        to_visit = set((r, c) for _, r, c in trees)
        visited = set()
        queue = [(0, 0)]
        while queue:
            r, c = queue.pop()
            to_visit.discard((r, c))
            visited.add((r, c))
            for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:

                if 0 <= r1 < rows and 0 <= c1 < cols and forest[r1][c1] and (r1, c1) not in visited:
                    queue.append((r1, c1))
        if to_visit:
            return -1

        def distance(r1, c1, r2, c2):
            direct = abs(r1 - r2) + abs(c1 - c2)
            diversions = 0
            queue = [(r1, c1)]
            next_queue = []
            visited = set()
            while True:
                if not queue:
                    queue, next_queue = next_queue, []
                    diversions += 1
                r1, c1 = queue.pop()
                if (r1, c1) == (r2, c2):
                    return direct + diversions * 2
                if (r1, c1) in visited:
                    continue
                visited.add((r1, c1))
                for r1, c1, closer in (r1 + 1, c1, r1 < r2), (r1 - 1, c1, r1 > r2), (r1, c1 + 1, c1 < c2), (
                        r1, c1 - 1, c1 > c2):
                    if 0 <= r1 < rows and 0 <= c1 < cols and forest[r1][c1]:
                        (queue if closer else next_queue).append((r1, c1))
        result = 0
        r1, c1 = 0, 0
        for _, r2, c2 in trees:
            result += distance(r1, c1, r2, c2)
            r1, c1 = r2, c2
        return result
