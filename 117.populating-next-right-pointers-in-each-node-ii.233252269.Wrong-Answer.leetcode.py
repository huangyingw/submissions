class Solution:
    def connect(self, root):
        if root == None:
            return
        queue = [root]
        queue.append(None)
        while queue:
            front = queue.pop(0)
            if front is not None:
                front.next = queue[0]
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            elif queue:
                queue.append(None)
class Solution:
    def connect(self, root):
        if not root:
            return None
        root.next = None
        while root:
            temp = root
            while temp:
                if temp.left:
                    if temp.right:
                        temp.left.next = temp.right
                    else:
                        temp.left.next = self.getNext(temp)
                if temp.right:
                    temp.right.next = self.getNext(temp)
                temp = temp.next
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = self.getNext(root)
    def getNext(self, node):
        node = node.next
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None
