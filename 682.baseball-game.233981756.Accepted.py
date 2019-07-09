_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        for op in ops:
            if op == "+":
                points.append(points[-1] + points[-2])
            elif op == "D":
                points.append(2 * points[-1])
            elif op == "C":
                points.pop()
            else:
                points.append(int(op))
        return sum(points)
