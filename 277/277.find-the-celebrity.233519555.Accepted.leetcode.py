def knows(a, b):
    return


class Solution(object):
    def findCelebrity(self, n):

        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i == candidate:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate
