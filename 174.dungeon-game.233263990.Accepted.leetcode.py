class Solution(object):
    def calculateMinimumHP(self, dungeon):
        rows, cols = len(dungeon), len(dungeon[0])
        for r in range(rows - 1):
            dungeon[r].append(float('inf'))
        dungeon.append([float('inf') for _ in range(cols + 1)])
        dungeon[rows - 1].append(1)
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                dungeon[r][c] = max(1, -dungeon[r][c] + min(dungeon[r + 1][c], dungeon[r][c + 1]))
        return dungeon[0][0]
