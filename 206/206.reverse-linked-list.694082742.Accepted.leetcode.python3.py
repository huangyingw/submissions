class Solution(object):
    def reverseList(self, head):
        def dfs(head):
            if not head or not head.next:
                return head
            second = head.next
            ret = dfs(second)
            second.next = head
            return ret
        result = dfs(head)
        if head:
            head.next = None
        return result
