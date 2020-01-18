class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        indexA = indexB = 0
        res = []
        while indexA < len(A) and indexB < len(B):
            start = max(A[indexA][0], B[indexB][0])
            end = min(A[indexA][1], B[indexB][1])
            if start <= end:
                res.append([start, end])
            if A[indexA][1] < B[indexB][1]:
                indexA += 1
            else:
                indexB += 1
        return res
