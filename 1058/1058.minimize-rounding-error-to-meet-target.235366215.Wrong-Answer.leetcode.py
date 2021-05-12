class Solution(object):
    def minimizeError(self, prices, target):
        base = 0
        remainders = []
        for price in prices:
            integer, remainder = price.split(".")
            base += int(integer)
            if remainder != "000":
                remainders.append(int(remainder))
        if target < base or target > base + len(remainders):
            return "-1"
        remainders.sort(reverse=True)
        result = 0
        i = 0
        while i < len(remainders) and base + i < target:
            result += 1000 - remainders[i]
            i += 1
        result += sum(remainders[i:])
        return "{:.3f}".format(result // 1000)
