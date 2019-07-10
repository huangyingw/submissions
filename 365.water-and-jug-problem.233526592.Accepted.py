class Solution(object):
    def canMeasureWater(self, x, y, z):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        if z == 0:
            return True
        g = gcd(x, y)
        if g == 0:
            return False
        return z % g == 0 and z <= x + y
