class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.squareSum(self.squareSum(n))
        while fast != slow:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
        return fast == 1
    def squareSum(self, n):
        new_no = 0
        while n:
            new_no += (n % 10) * (n % 10)
            n //= 10
        return new_no
class Solution1:
    def isHappy(self, n):
        while n > 6:
            nextN = 0
            while(n):
                nextN += (n % 10) * (n % 10)
                n //= 10
            n = nextN
        return n == 1
class Solution2:
    def isHappy(self, n: int) -> bool:
        temp = set()
        while n:
            if n == 1:
                return True
            temp.add(n)
            new_no = self.squareSum(n)
            if new_no in temp:
                return False
            n = new_no
    def squareSum(self, n):
        new_no = 0
        while n:
            new_no += (n % 10) * (n % 10)
            n //= 10
        return new_no
