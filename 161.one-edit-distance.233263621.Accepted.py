







class Solution(object):
    def isOneEditDistance(self, s, t):

        diff = len(s) - len(t)
        if abs(diff) > 1:
            return False
        edit = False
        if diff == 0:
            for c_s, c_t in zip(s, t):
                if c_s != c_t:
                    if edit:
                        return False
                    edit = True
            return edit
        else:
            long, short = s, t
            if diff < 0:
                long, short = short, long
            i = 0
            while i < len(short) and long[i] == short[i]:
                i += 1
            return long[i + 1:] == short[i:]
