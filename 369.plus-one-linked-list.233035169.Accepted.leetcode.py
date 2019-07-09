






class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        place_stop, tail = dummy, dummy

        while tail.next is not None:
            tail = tail.next
            if tail.val != 9:
                place_stop = tail
        if tail.val != 9:

            tail.val += 1
        else:

            place_stop.val += 1
            place_stop = place_stop.next

            while place_stop is not None:
                place_stop.val = 0
                place_stop = place_stop.next
        if dummy.val == 0:
            return dummy.next
        return dummy
