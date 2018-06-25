class Solution(object):
    def partition(self, s):
        current = []
        result = []

        def isPalindrome(s):
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
            return True

        def dfs(start):
            if start == len(s):
                result.append(list(current))

            for index in range(start, len(s)):
                if isPalindrome(s[start:index]):
                    current.append(s[start:index])
                    dfs(index + 1)
                    current.pop()
        dfs(0)
        return result
