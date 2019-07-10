class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx
        if tx == sx and (ty - sy) % sx == 0:
            return True
        return ty == sy and (tx - sx) % sy == 0
