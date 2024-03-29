class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp
        if fast:
            slow = slow.next
        while rev:
            rev = rev.next
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev
