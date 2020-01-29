class Solution:
    def isPalindrome(self, s):
        processedString = []
        for c in s:
            if c.isalnum():
                processedString.append(c.lower())
        l = len(processedString)
        for i in range(0, l / 2):
            if processedString[i] != processedString[l - 1 - i]:
                return False
        return True
