






class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        stack = [result[-1]]
        ans = [0]
        for val in range(len(result) - 2, -1, -1):
            if result[val] < stack[-1]:
                ans.append(stack[-1])
            else:
                while stack and stack[-1] <= result[val]:
                    stack.pop()
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(0)
            stack.append(result[val])
        return ans[::-1]
