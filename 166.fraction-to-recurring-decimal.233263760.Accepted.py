






class Solution(object):
    def fractionToDecimal(self, numerator, denominator):

        if denominator == 0:
            return None
        decimal = []
        if numerator * denominator < 0:
            decimal.append('-')
        output, remainder = divmod(abs(numerator), abs(denominator))
        decimal.append(str(output))
        if remainder == 0:
            return "".join(decimal)
        decimal.append('.')
        seen = {}
        while remainder != 0:
            if remainder in seen:
                return "".join(decimal[:seen[remainder]] + ['('] + decimal[seen[remainder]:] + [')'])
            seen[remainder] = len(decimal)
            output, remainder = divmod(remainder * 10, abs(denominator))
            decimal.append(str(output))
        return "".join(decimal)
