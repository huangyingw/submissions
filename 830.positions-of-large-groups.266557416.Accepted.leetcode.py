class Solution(object):
    def largeGroupPositions(self, S):
        if not S:
            return []
        result = []
        count = 1
        prevChar = S[0]
        index_i = 0
        for index in range(1, len(S)):
            if S[index] == prevChar:
                count += 1
            else:
                if count >= 3:
                    result.append([index_i, index - 1])
                count = 1
                prevChar = S[index]
                index_i = index
        if count >= 3:
            result.append([index_i, len(S) - 1])
        return result
