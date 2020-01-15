import random


class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        res = None
        length = 0
        cur = self.head
        while cur:
            num = random.randint(0, length)
            if num == 0:
                res = cur.val
            cur = cur.next
            length += 1
        return res
