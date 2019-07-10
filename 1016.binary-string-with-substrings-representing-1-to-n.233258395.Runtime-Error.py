











class Solution(object):
    def queryString(self, S, N):

        for num in range(N, 0, -1):
            if bin(num)[2:] not in S:
                return False
        return True
