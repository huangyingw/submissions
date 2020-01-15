class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        return self.helper(s1, s2, s3, 0, 0, {})

    def helper(self, s1, s2, s3, i, j, memo):
        if i >= len(s1) or j >= len(s2):
            return s1[i:] + s2[j:] == s3[i + j:]
        if (i, j) in memo:
            return memo[(i, j)]
        result = False
        if s1[i] == s3[i + j] and self.helper(s1, s2, s3, i + 1, j, memo):
            result = True
        elif s2[j] == s3[i + j] and self.helper(s1, s2, s3, i, j + 1, memo):
            result = True
        memo[(i, j)] = result
        return result
