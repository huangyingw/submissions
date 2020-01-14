class Solution(object):
    def findCircleNum(self, M):
        def node_id(node, n):
            return node[0] * n + node[1]
        def find_set(x):
            if set[x] != x:
                set[x] = find_set(set[x])
            return set[x]
        def union_set(x, y):
            x_root, y_root = find_set(x), find_set(y)
            set[min(x_root, y_root)] = max(x_root, y_root)
        number = len(M)
        set = range(len(M))
        for i in xrange(len(M)):
            for j in xrange(len(M)):
                if M[i][j] and i != j:
                    if find_set(i) != find_set(j):
                        union_set(i, j)
                        number -= 1
        return number
