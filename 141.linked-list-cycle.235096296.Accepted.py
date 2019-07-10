'''
	Given a linked list, determine if it has a cycle in it.
	Follow up:
	Can you solve it without using extra space?
'''







class Solution(object):
    def hasCycle(self, head):

        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
