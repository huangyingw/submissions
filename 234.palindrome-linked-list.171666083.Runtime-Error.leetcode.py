class Solution(object):
    def reverseList(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
    def isPalindrome(self, head):
        fast, slow = head
        while fast and slow:
            fast = fast.next.next
            slow = slow.next
        end = self.reverseList(slow)
        while head and end:
            if head.val != end.val:
                return False
        return True
