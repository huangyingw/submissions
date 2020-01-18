class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        ref = head
        while n > 0:
            ref = ref.next
