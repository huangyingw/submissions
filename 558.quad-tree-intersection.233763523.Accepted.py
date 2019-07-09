_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        children = [topLeft, topRight, bottomLeft, bottomRight]
        values = [child.val for child in children]
        leaves = [child.isLeaf for child in children]
        if all(leaves) and (sum(values) == 0 or sum(values) == 4):
            return Node(topLeft.val, True, None, None, None, None)

        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
