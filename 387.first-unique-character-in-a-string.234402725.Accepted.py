
class Solution:

    def firstUniqChar(self, s):

        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1




    def firstUniqChar(self, s):

        res = []
        ret = len(s)
        for i in set(s):
            if s.count(i) == 1:
                res.append(i)
        if not res:
            return -1
        for i in res:
            ret = min(ret, s.index(i))
        return ret




    def firstUniqChar(self, s):
        if not s:
            return -1
        L = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            left = s.find(c)
            right = s.rfind(c)
            if 0 <= left < L and left == right:
                L = left
        return L if L < len(s) else -1
