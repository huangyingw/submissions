class Solution(object):
    def gardenNoAdj(self, N, paths):
        plant = [1, 2, 3, 4]
        result = [0 for _ in range(N)]
        if not paths:
            return [plant[index % 4] for index in range(N)]
        change = {}
        update = []
        for path in paths:
            x, y = path[0] - 1, path[1] - 1
            if x in change:
                change[x].append(y)
            else:
                change[x] = [y]
            if y in change:
                change[y].append(x)
            else:
                change[y] = [x]
        for garden in range(N):
            color_used = []
            if garden in change:
                subgarden = change[garden]
                for subgarden in change[garden]:
                    if result[subgarden]:
                        color_used.append(result[subgarden])
            color_rem = list(set([1, 2, 3, 4]) - set(color_used))
            for color in color_rem:
                result[garden] = color
                break
        return result
