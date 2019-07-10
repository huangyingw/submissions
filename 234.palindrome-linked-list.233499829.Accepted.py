







class Solution(object):
    def isPalindrome(self, head):

        fast, slow = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = rev
            rev = slow
            slow = next_slow


        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
