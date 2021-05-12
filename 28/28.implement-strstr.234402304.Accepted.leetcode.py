class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
