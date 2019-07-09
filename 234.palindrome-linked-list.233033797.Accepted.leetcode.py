






class Solution(object):

















    def isPalindrome(self, head):






        if head is None:
            return True
        p1, p2 = head, head
        p3, pre = p1.next, p1
        while p2.next is not None and p2.next.next is not None:
            p2 = p2.next.next
            pre = p1
            p1 = p3
            p3 = p3.next
            p1.next = pre
        if p2.next is None:
            p1 = p1.next
        while p3 is not None:
            if p1.val != p3.val:
                return False
            p1 = p1.next
            p3 = p3.next
        return True
