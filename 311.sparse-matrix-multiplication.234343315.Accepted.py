class Solution:
    def multiply(self, A, B):

        if not A or not B:
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("Two matrice don't match")
        table_B = {}
        for i, row in enumerate(B):
            table_B[i] = {}
            for j, element in enumerate(row):
                if element:
                    table_B[i][j] = element
        C = [[0] * l for _ in range(m)]
        for i, row in enumerate(A):
            for y, item in enumerate(row):
                if item:
                    for j, v in table_B[y].items():
                        C[i][j] += item * v
        return C
