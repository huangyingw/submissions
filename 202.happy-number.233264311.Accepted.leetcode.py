class Solution(object):
    def isHappy(self, n):
        if n == 1:
            return True, 1
        slow = sum([int(c) * int(c) for c in str(n)])
        fast = sum([int(c) * int(c) for c in str(slow)])
        while fast != slow:
            slow = sum([int(c) * int(c) for c in str(slow)])
            fast = sum([int(c) * int(c) for c in str(fast)])
            fast = sum([int(c) * int(c) for c in str(fast)])
        return slow == 1
class Solution2(object):
    def isHappy(self, n):
        while True:
            if n == 1:
                return True
            if n == 4:
                return False
            n = sum([int(c) * int(c) for c in str(n)])
