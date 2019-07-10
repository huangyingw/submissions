import random


class Solution(object):
    def __init__(self, head):
        self.head = head
        self.count = 0
        while head:
            self.count += 1
            head = head.next

    def getRandom(self):
        randnode = random.randint(0, self.count - 1)
        node = self.head
        for _ in range(randnode):
            node = node.next
        return node.val
