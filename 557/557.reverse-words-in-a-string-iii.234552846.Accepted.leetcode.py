class Solution:
    def reverseWords(self, s):
        rs = s[::-1]
        rs = rs.split()
        result = ""
        for i in rs[::-1]:
            result += " " + i
        return result[1:]
