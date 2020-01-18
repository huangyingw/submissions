class Solution:
    def sortedListToBST(self, head):
        return self.dfs(head, None)

    def dfs(self, head, tail):
        if head == tail:
            return None
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.dfs(head, slow)
        root.right = self.dfs(slow.next, tail)
        return root
