class Solution:
    def connect(self, root):
        head = None
        previous = None
        current = root
        while current is not None:
            while current is not None:
                if current.left is not None:
                    if previous is not None:
                        previous.next = current.left
                    else:
                        head = current.left
                    previous = current.left
                if current.right is not None:
                    if previous is not None:
                        previous.next = current.right
                    else:
                        head = current.right
                    previous = current.right
                current = current.next
            current = head
            head = None
            previous = None
