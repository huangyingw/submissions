class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object):
    def intervalIntersection(self, A, B):
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            last_start = max(A[i].start, B[j].start)
            first_end = min(A[i].end, B[j].end)
            if last_start <= first_end:
                result.append(Interval(s=last_start, e=first_end))
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
        return result
