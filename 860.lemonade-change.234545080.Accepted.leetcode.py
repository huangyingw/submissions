class Solution:
    def lemonadeChange(self, bills):
        store_five = 0
        store_ten = 0
        for bill in bills:
            if bill == 5:
                store_five += 1
            elif bill == 10:
                store_ten += 1
                store_five -= 1
            else:
                if store_ten > 0:
                    store_ten -= 1
                    store_five -= 1
                else:
                    store_five -= 3
            if store_five < 0:
                return False
        return True
t = Solution()
