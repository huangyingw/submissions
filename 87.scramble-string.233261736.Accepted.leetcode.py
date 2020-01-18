from collections import Counter


class Solution(object):
    def isScramble(self, s1, s2):
        count1 = Counter(s1)
        for c in s2:
            if c not in count1:
                return False
            count1[c] -= 1
            if count1[c] < 0:
                return False
        if s1 == s2:
            return True
        for partition in range(1, len(s1)):
            s1_l = s1[:partition]
            s1_r = s1[partition:]
            s2_l = s2[:partition]
            s2_r = s2[partition:]
            s2_l_swap = s2[:-partition]
            s2_r_swap = s2[-partition:]
            if (self.isScramble(s1_l, s2_l) and self.isScramble(s1_r, s2_r)) or (self.isScramble(s1_l, s2_r_swap) and self.isScramble(s1_r, s2_l_swap)):
                return True
        return False
