class Solution(object):
    def mirrorReflection(self, p, q):
        k = 1
        while (k * q) % p != 0:
            k += 1
        if k % 2 == 0:
            return 2
        if ((k * q) // p) % 2 == 0:
            return 0
        return 1
