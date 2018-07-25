class Solution(object):
    def reverseList(self, head):
        def helper(head):
            if not head or not head.next:
                return head

            second = head.next
            ret = helper(second)
            second.next = head
            return second

        result = helper(head)
        head.next = None
        return result
