_author_ = 'jake'
_project_ = 'leetcode'



















class Solution(object):

    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    rows = height(root)
    cols = 2 ** rows - 1
    result = [["" for _ in range(cols)] for _ in range(rows)]

    def place(node, r, c):
        if not node:
            return
        result[r][c] = str(node.val)
        shift = 2 ** (rows - r - 2)
        place(node.left, r + 1, c - shift)
        place(node.right, r + 1, c + shift)
    place(root, 0, cols // 2)
    return result
