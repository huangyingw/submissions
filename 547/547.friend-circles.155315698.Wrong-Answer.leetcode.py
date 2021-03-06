class Solution(object):
    def findCircleNum(self, M):
        def find_set(x):
            return set[x]

        def union_set(x, y):
            x_root, y_root = find_set(x), find_set(y)
            set[min(x_root, y_root)] = max(x_root, y_root)
        number = len(M)
        set = range(len(M))
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] and i != j:
                    if find_set(i) != find_set(j):
                        union_set(i, j)
                        number -= 1
        return number
