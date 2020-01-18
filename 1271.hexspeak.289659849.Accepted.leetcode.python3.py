class Solution(object):
    def toHexspeak(self, num):
        s = format(int(num), "X")
        if any(str(i) in s for i in range(3, 10)):
            return "ERROR"
        s = s.replace("0", "O")
        return s.replace("1", "I")
