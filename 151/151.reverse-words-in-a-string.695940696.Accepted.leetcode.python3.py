class Solution(object):
    def reverseWords(self, s):
        arr = s.split(" ")
        sb = ""
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != "":
                sb += arr[i]
                sb += " "
        return sb[: -1]
