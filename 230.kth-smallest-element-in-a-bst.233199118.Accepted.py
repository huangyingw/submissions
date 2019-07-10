'''
	Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
	Note:
	You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
	Example 1:
	Input: root = [3,1,4,null,2], k = 1
	Output: 1
'''








class Solution(object):
    def kthSmallest(self, root, k):

        if not root:
            return 0
        stack = [root]
        count, curr = 0, root
        while stack:
            if curr.left:
                stack.append(curr.left)
                curr = curr.left
            else:
                val = stack.pop()
                count += 1
                if count == k:
                    return val.val
                if val.right:
                    stack.append(val.right)
                    curr = val.right
        return float('-inf')
