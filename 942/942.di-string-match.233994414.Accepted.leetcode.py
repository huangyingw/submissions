class Solution(object):
    def diStringMatch(self, S):
        result = []
        low, high = 0, len(S)
        for c in S:
            if c == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        return result + [low]
