class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


class SolutionKMP:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i, j, l = 1, 0, len(s)
        lookup = [0] * (l + 1)
        while i < l:
            if s[i] == s[j]:
                i += 1
                j += 1
                lookup[i] = j
            elif j == 0:
                i += 1
            else:
                j = lookup[j]
        return lookup[l] and not lookup[l] % (l - lookup[l])
