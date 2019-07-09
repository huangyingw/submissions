_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    """
    :type n: int
    :type k: int
    :rtype: str
    """

    def crackSafe(self, n, k):
        seen = set()
        digits = [str(i) for i in range(k)]
        result = []

        def dfs(node):
            for x in digits:
                pattern = node + x
                if pattern not in seen:
                    seen.add(pattern)
                    dfs(pattern[1:])
                    result.append(x)
        dfs("0" * (n - 1))
        return "".join(result) + "0" * (n - 1)
