class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        rows, cols = set(), set()
        for r, c in blocked + [source, target]:
            rows.add(r)
            cols.add(c)
        rows, cols = sorted(list(rows)), sorted(list(cols))
        row_to_compressed, col_to_compressed = {}, {}
        new_row, new_col = int(rows[0] != 0), int(cols[0] != 0)
        for i, r in enumerate(rows):
            if i != 0 and rows[i - 1] != r - 1:
                new_row += 1
            row_to_compressed[r] = new_row
            new_row += 1
        for i, c in enumerate(cols):
            if i != 0 and cols[i - 1] != c - 1:
                new_col += 1
            col_to_compressed[c] = new_col
            new_col += 1
        blocked = {(row_to_compressed[r], col_to_compressed[c]) for r, c in blocked}
        source = (row_to_compressed[source[0]], col_to_compressed[source[1]])
        target = (row_to_compressed[target[0]], col_to_compressed[target[1]])
        if new_row != 10 ** 6 + 1:
            new_row += 1
        if new_col != 10 ** 6 + 1:
            new_col += 1
        frontier, back, visited = {source, }, {target, }, set()
        while frontier and back:
            if frontier & back - blocked:
                return True
            if len(frontier) > len(back):
                frontier, back = back, frontier
            new_frontier = set()
            for r, c in frontier:
                if (r, c) in blocked or (r, c) in visited:
                    continue
                if r < 0 or r >= new_row or c < 0 or c >= new_col:
                    continue
                visited.add((r, c))
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    new_frontier.add((r + dr, c + dc))
            frontier = new_frontier
        return False
