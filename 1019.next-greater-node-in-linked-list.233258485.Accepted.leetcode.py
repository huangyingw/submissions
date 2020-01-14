class Solution(object):
    def nextLargerNodes(self, head):
        result = []
        stack = []
        node = head
        i = 0
        while node:
            result.append(0)
            while stack and stack[-1][1] < node.val:
                j, _ = stack.pop()
                result[j] = node.val
            stack.append((i, node.val))
            i += 1
            node = node.next
        return result
