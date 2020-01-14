class Solution(object):
    def digitsCount(self, d, low, high):
        def count_digits(n):
            if n == 0 or (d == 0 and n <= 10):
                return 0
            result = 0
            prefix, units = divmod(n, 10)
            if units > d:
                result += 1
            if prefix > 0:
                result += str(prefix).count(str(d)) * units
            result += prefix if d else prefix - 1
            result += count_digits(prefix) * 10
            return result
        return count_digits(high + 1) - count_digits(low)
