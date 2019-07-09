_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        group = [i for i in range(n)]

        def get_group(x):
            while group[x] != x:
                group[x] = group[group[x]]
                x = group[x]
            return x
        for i in range(1, n):
            for j in range(i):
                if M[i][j] == 1:
                    group[get_group(i)] = get_group(j)
        return len(set(get_group(i) for i in range(n)))


class Solution2(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1:
                    if j not in seen:
                        seen.add(j)
                        dfs(j)
        circles = 0
        seen = set()
        for i in range(len(M)):
            if i not in seen:
                circles += 1
                dfs(i)
        return circles
