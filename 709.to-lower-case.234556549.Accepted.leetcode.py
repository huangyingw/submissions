class Solution:
    def toLowerCase(self, str):
        return ''.join([chr(ord('a') + ord(s) - ord('A')) if ord(s) <= ord('Z') and ord(s) >= ord('A') else s for s in str])
