class Solution(object):
    def swapPairs(self, head):

        if head is None or head.next is None:
            return head
        nextHead = head.next.next
        newHead = head.next
        head.next.next = head
        head.next = self.swapPairs(nextHead)
        return newHead
