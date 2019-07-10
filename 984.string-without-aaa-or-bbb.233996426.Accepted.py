











class Solution:
    def strWithout3a3b(self, a, b):

        result = []
        diff = a - b
        if diff > 0:
            groups = min(diff, b)
            result = ["aab"] * groups
            a -= 2 * groups
            b -= groups
        elif diff < 0:
            groups = min(-diff, a)
            result = ["bba"] * groups
            b -= 2 * groups
            a -= groups
        pairs = min(a, b)
        result += ["ab"] * pairs
        a -= pairs
        b -= pairs
        result += ["a"] * a + ["b"] * b
        return "".join(result)
