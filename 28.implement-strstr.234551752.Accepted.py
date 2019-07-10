

class Solution(object):
    def strStr(self, haystack, needle):

        if needle == ""or needle == haystack:
            return 0
        l = len(needle)
        for i in range(0, (len(haystack) - l + 1)):
            if haystack[i:i + l] == needle:
                return i
        return -1
