class Solution:
    def validTree(self, n, edges):

        union_arr = range(n)

        def find_union(p):
            if union_arr[p] == p:
                return p
            else:
                return find_union(union_arr[p])
        for p1, p2 in edges:
            p1_set = find_union(p1)
            p2_set = find_union(p2)
            if p1_set == p2_set:
                return False
            union_arr[p1_set] = p2_set
        return len(edges) == n - 1
