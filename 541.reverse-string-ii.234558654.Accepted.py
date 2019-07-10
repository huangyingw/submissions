

class Solution(object):
    def reverseStr(self, s, k):

        res = []
        n = len(s)
        revFlag = 1
        i = 0
        while i < n:
            last = min(i + k, n)
            if revFlag:
                if i > 0:
                    res.append(s[(last - 1):(i - 1):-1])
                else:
                    res.append(s[(last - 1)::-1])
            else:
                res.append(s[i:last])
            revFlag = 1 - revFlag
            i += k
        return "".join(res)
