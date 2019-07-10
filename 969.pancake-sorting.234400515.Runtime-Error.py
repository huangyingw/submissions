



class Solution(object):
    def pancakeSort1(self, A):
        ans = []
        length = len(A)
        B = sorted(range(0, length), key=lambda index: -A[index])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f + 1 - i
            ans.extend([i, length])
            length -= 1
        return ans

    def pancakeSort2(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res
