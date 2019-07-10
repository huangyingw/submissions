


class Solution(object):
    def minFlipsMonoIncr(self, S):
        ones = [0]
        for char in S:
            ones.append(ones[-1] + int(char))
        result = float('inf')
        for index in range(len(ones)):
            zeroes = len(S) - index - (ones[-1] - ones[index])
            result = min(zeroes + ones[index], result)
        return result
