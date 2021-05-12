class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return (x * y) // gcd(x, y)
        a, b, c = sorted([a, b, c])
        ab, ac, bc = lcm(b, a), lcm(c, a), lcm(c, b)
        abc = lcm(bc, a)

        def ugly_less_or_equal(x):
            result = (x // a) + (x // b) + (x // c)
            result -= (x // ab) + (x // ac) + (x // bc)
            result += x // abc
            return result
        lower, upper = 1, 2 * 10 ** 9
        while lower < upper:
            mid = (lower + upper) // 2
            if ugly_less_or_equal(mid) >= n:
                upper = mid
            else:
                lower = mid + 1
        return lower
