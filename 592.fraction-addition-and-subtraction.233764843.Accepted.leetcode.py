class Solution(object):
    def fractionAddition(self, expression):
        def GCD(a, b):
            div, mod = divmod(a, b)
            if mod == 0:
                return b
            return GCD(b, mod)
        result = [0, 1]
        start = 0
        while start < len(expression):
            end = start
            while expression[end + 1] != "/":
                end += 1
            fraction = [int(expression[start:end + 1])]
            start = end = end + 2
            while end + 1 < len(expression) and expression[end + 1] not in ["+", "-"]:
                end += 1
            fraction.append(int(expression[start:end + 1]))
            lcm = fraction[1] * result[1] / GCD(fraction[1], result[1])
            result = [(result[0] * lcm / result[1]) + (fraction[0] * lcm / fraction[1]), lcm]
            start = end + 1
        if result[0] == 0:
            return "0/1"
        gcd = GCD(result[0], result[1])
        return str(result[0] / gcd) + "/" + str(result[1] / gcd)
