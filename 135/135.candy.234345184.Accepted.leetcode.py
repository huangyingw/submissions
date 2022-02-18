class Solution:

    def candy(self, ratings):
        up, down, res, peak = 0, 0, 1, 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                res += up + 1
                peak = up
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                res += 1
            else:
                down += 1
                up = 0
                diff = -1 if peak >= down else 0
                res += 1 + down + diff
        return res
