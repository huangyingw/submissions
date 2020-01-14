class Excel(object):
    def _indices(self, r, c):
        return [r - 1, ord(c) - ord("A")]
    def __init__(self, H, W):
        rows, cols = self._indices(H, W)
        self.excel = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    def set(self, r, c, v):
        r, c, = self._indices(r, c)
        self.excel[r][c] = v
    def get(self, r, c):
        r, c = self._indices(r, c)
        return self.get_i(r, c)
    def get_i(self, r, c):
        contents = self.excel[r][c]
        if isinstance(contents, int):
            return contents
        total = 0
        for cells in contents:
            cell_range = cells.split(":")
            r1, c1 = self._indices(int(cell_range[0][1:]), cell_range[0][0])
            if len(cell_range) == 1:
                r2, c2 = r1, c1
            else:
                r2, c2 = self._indices(int(cell_range[1][1:]), cell_range[1][0])
            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    total += self.get_i(row, col)
        return total
    def sum(self, r, c, strs):
        r, c = self._indices(r, c)
        self.excel[r][c] = strs
        return self.get_i(r, c)
