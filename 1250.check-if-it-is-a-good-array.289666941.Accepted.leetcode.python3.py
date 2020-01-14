class Solution(object):
    def isGoodArray(self, nums):
        def calc_gcd(a, b):
            while a > 0:
                a, b = b % a, a
            return b
        gcd = nums[0]
        for num in nums:
            gcd = calc_gcd(num, gcd)
            if gcd == 1:
                return True
        return False
