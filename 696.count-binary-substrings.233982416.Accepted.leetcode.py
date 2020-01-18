class Solution(object):
    def countBinarySubstrings(self, s):
        seq, prev_seq = 1, 0
        count = 0
        for i, c in enumerate(s[1:], 1):
            if c != s[i - 1]:
                count += min(seq, prev_seq)
                seq, prev_seq = 1, seq
            else:
                seq += 1
        return count + min(seq, prev_seq)
