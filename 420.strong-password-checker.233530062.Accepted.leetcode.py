class Solution(object):
    def strongPasswordChecker(self, s):
        upper, lower, digit = False, False, False
        subs, i = 0, 0
        singles, doubles = 0, 0
        while i < len(s):
            if s[i].isdigit():
                digit = True
            if s[i].isupper():
                upper = True
            if s[i].islower():
                lower = True
            if i >= 2 and s[i] == s[i - 1] == s[i - 2]:
                seq = 2
                while i < len(s) and s[i] == s[i - 1]:
                    seq += 1
                    i += 1
                subs += seq / 3
                if seq % 3 == 0:
                    singles += 1
                if seq % 3 == 1:
                    doubles += 1
            else:
                i += 1
        types_missing = 3 - (digit + upper + lower)
        if len(s) < 6:
            return max(types_missing, 6 - len(s))
        if len(s) <= 20:
            return max(types_missing, subs)
        deletions = len(s) - 20
        subs -= min(deletions, singles)
        subs -= min(max(deletions - singles, 0), doubles * 2) / 2
        subs -= max(deletions - singles - 2 * doubles, 0) / 3
        return deletions + max(types_missing, subs)
