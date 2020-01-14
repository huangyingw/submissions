class Solution:
    def shiftingLetters(self, S, shifts):
        temp = list(S)
        length = len(shifts)
        offset = 0
        for i in range(length - 1, -1, -1):
            offset += shifts[i]
            offset %= 26
            temp[i] = chr(ord(temp[i]) + offset if ord(temp[i]) + offset <= 122 else ord(temp[i]) + offset - 26)
        return ''.join(temp)
    def shiftingLetters2(self, S, shifts):
        for i in range(len(shifts) - 1)[::-1]:
            shifts[i] += shifts[i + 1]
        return "".join(chr((ord(c) - 97 + s) % 26 + 97) for c, s in zip(S, shifts))
