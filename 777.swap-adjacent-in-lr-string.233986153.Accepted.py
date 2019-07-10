











class Solution(object):
    def canTransform(self, start, end):

        if len(start) != len(end):
            return False
        left, right = 0, 0
        for c1, c2 in zip(start, end):
            if c1 == "L":
                left += 1
            elif c1 == "R":
                right += 1
            if c2 == "L":
                left -= 1
            elif c2 == "R":
                right -= 1
            if left > 0 or right < 0:
                return False
            if left < 0 and right > 0:
                return False
        return left == 0 and right == 0
