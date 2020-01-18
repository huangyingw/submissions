class Solution(object):
    def alphabetBoardPath(self, target):
        def location(char):
            val = ord(char) - ord("a")
            return divmod(val, 5)
        result = []
        row, col = 0, 0
        for char in target:
            r, c = location(char)
            if c < col:
                result += ["L"] * (col - c)
            if r < row:
                result += ["U"] * (row - r)
            if c > col:
                result += ["R"] * (c - col)
            if r > row:
                result += ["D"] * (r - row)
            row, col = r, c
            result.append("!")
        return "".join(result)
