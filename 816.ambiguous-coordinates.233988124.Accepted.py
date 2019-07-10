




















class Solution(object):
    def ambiguousCoordinates(self, S):

        def insert_decimal(s):
            if s == "0":
                return [s]
            if s[0] == "0" and s[-1] == "0":
                return []
            if s[0] == "0":
                return ["0." + s[1:]]
            if s[-1] == "0":
                return [s]
            return [s[:i] + "." + s[i:] for i in range(1, len(s))] + [s]
        S = S[1:-1]
        result = []
        for i in range(1, len(S)):
            left = insert_decimal(S[:i])
            right = insert_decimal(S[i:])
            result += ["(" + ", ".join([l, r]) + ")" for l in left for r in right]
        return result
