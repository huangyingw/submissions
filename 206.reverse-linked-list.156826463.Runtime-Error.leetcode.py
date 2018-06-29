class Solution(object):
    def reverseList(self, head):

        def helper(head):
            if not head or not head.next:
                return

            second = head.next
            ret = helper(second)
            second.next = head
            return ret

        result = helper(head)
        head.next = None
        return result
