class Solution(object):
    def reverseList(self, head):
        def helper(head):
            if not head or not head.next:
                return head

            second = head.next
            ret = helper(second)
            second.next = head
            return ret

        if not head:
            return head

        result = helper(head)
        head.next = None
        return result
