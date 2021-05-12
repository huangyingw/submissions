class Solution(object):
    def validPalindrome(self, s):
        n = len(s)
        i = 0
        while i < n // 2:
            if s[i] != s[n - 1 - i]:
                del_front = s[i + 1:n - i]
                del_back = s[i:n - 1 - i]
                return del_front == del_front[::-1] or del_back == del_back[::-1]
            i += 1
        return True
