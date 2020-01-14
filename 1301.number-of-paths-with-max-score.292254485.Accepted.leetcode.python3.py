class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10 ** 9 + 7
        rows, cols = len(board), len(board[0])
        visited = {}
        def helper(r, c):
            if r < 0 or c < 0 or board[r][c] == "X":
                return [0, 0]
            if (r, c) in visited:
                return visited[(r, c)]
            if r == 0 and c == 0:
                return [0, 1]
            up_max, up_paths = helper(r - 1, c)
            left_max, left_paths = helper(r, c - 1)
            up_left_max, up_left_paths = helper(r - 1, c - 1)
            max_value, max_count_paths = 0, 0
            if up_paths + left_paths + up_left_paths > 0:
                max_value = max(up_max, left_max, up_left_max)
                if up_max == max_value:
                    max_count_paths += up_paths
                if left_max == max_value:
                    max_count_paths += left_paths
                if up_left_max == max_value:
                    max_count_paths += up_left_paths
                max_value += int(board[r][c]) if r < rows - 1 or c < cols - 1 else 0
            visited[(r, c)] = [max_value, max_count_paths]
            return [max_value, max_count_paths % MOD]
        return helper(rows - 1, cols - 1)
