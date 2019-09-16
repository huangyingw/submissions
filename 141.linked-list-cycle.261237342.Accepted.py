class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False
