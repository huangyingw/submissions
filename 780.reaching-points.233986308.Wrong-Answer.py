_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx
        if tx == sx and (ty - sy) % sx == 0:
            return True
        return ty == sy and (tx - sx) % sy == 0
