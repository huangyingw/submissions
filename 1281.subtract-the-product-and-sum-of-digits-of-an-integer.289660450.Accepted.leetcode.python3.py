class Solution(object):
    def subtractProductAndSum(self, n):
        product, total = 1, 0
        while n > 0:
            n, digit = divmod(n, 10)
            product *= digit
            total += digit
        return product - total
