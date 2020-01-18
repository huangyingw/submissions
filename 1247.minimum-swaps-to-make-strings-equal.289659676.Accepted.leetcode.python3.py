class Solution(object):
    def minimumSwap(self, s1, s2):
        s1_excess_x, s1_excess_y = False, False
        result = 0
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            if c1 == "x":
                if s1_excess_x:
                    result += 1
                s1_excess_x = not s1_excess_x
            else:
                if s1_excess_y:
                    result += 1
                s1_excess_y = not s1_excess_y
        if s1_excess_x ^ s1_excess_y:
            return -1
        return result + int(s1_excess_x) + int(s1_excess_y)
