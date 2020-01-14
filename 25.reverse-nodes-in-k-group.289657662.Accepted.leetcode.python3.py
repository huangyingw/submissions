class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head
        count = 0
        dummyHead = ListNode(0)
        dummyHead.next = head
        begin = dummyHead
        while head:
            count += 1
            if count % k == 0:
                begin = self.reverseList(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummyHead.next
    def reverseList(self, begin, end):
        cur = begin.next
        prev = begin
        first = cur
        while cur != end:
            cur.next, prev, cur = prev, cur, cur.next
        begin.next = prev
        first.next = cur
        return first
class SolutionRecursive:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        newhead = head
        for i in range(k):
            if newhead == None:
                return head
            newhead = newhead.next
        connect = cur = head
        prev = None
        for i in range(k):
            cur.next, cur, prev = prev, cur.next, cur
        connect.next = self.reverseKGroup(newhead, k)
        return prev
