










class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        num1, num2 = 0, 0
        node = l1
        while node:
            num1 = num1 * 10 + node.val
            node = node.next
        node = l2
        while node:
            num2 = num2 * 10 + node.val
            node = node.next
        total = num1 + num2
        if total == 0:
            return ListNode(0)
        result = None
        while total:
            total, digit = divmod(total, 10)
            new_node = ListNode(digit)
            new_node.next = result
            result = new_node
        return result
