class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):

        if not head:
            return None
        cur = head.next if head.next else head
        prev = None
        while head and head.next:
            temp = head.next
            head.next = head.next.next
            temp.next = head
            head = head.next
            if prev:
                prev.next = temp
            prev = temp.next
        return cur

    def swapPairs_alt(self, head: ListNode) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        cur = newHead
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = a
        return newHead.next

    def swapPairs_recursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs_recursive(new_start)
        return head
