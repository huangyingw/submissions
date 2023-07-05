class Solution(object):
    def findJudge(self, N, trust):

        trust_count = [0] * (N + 1)
        for trustee, trusted in trust:
            trust_count[trusted] += 1
            trust_count[trustee] -= 1
        for person in range(1, N + 1):
            if trust_count[person] == N - 1:
                return person
        return -1
