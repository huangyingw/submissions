class Solution:
    def minFlipsMonoIncr(self, S):
        zeros, ones = S.count("0"), 0
        result = zeros
        for c in S:
            if c == "0":
                zeros -= 1
            else:
                ones += 1
            result = min(result, zeros + ones)
        return result
