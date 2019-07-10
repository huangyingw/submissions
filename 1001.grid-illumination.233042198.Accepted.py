_author_ = 'jake'
_project_ = 'leetcode'














from collections import defaultdict


class Solution(object):
    def gridIllumination(self, N, lamps, queries):

        lamps = {tuple(lamp) for lamp in lamps}
        x_lamps, y_lamps = defaultdict(int), defaultdict(int)
        up_diag_lamps, down_diag_lamps = defaultdict(int), defaultdict(int)

        for x, y in lamps:
            x_lamps[x] += 1
            y_lamps[y] += 1
            up_diag_lamps[x - y] += 1
            down_diag_lamps[x + y] += 1
        result = []
        for x, y in queries:
            illuminated = x_lamps[x] + y_lamps[y] + up_diag_lamps[x - y] + down_diag_lamps[x + y]
            result.append(min(illuminated, 1))
            if illuminated != 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (x + dx, y + dy) in lamps:
                            lamps.discard((x + dx, y + dy))
                            x_lamps[x + dx] -= 1
                            y_lamps[y + dy] -= 1
                            up_diag_lamps[x + dx - y - dy] -= 1
                            down_diag_lamps[x + dx + y + dy] -= 1
        return result
