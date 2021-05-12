class Solution(object):
    def shiftingLetters(self, S, shifts):
        s = [ord(c) - ord("a") for c in S]
        cumulative_shift = 0
        for i in range(len(s) - 1, -1, -1):
            cumulative_shift += shifts[i]
            s[i] = (s[i] + cumulative_shift) % 26
        return "".join(chr(c + ord("a")) for c in s)
