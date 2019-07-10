class Codec:
    def serialize(self, root):
        def serializeHelper(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = serializeHelper(root.left, string)
                string = serializeHelper(root.right, string)
            return string
        return serializeHelper(root, "")

    def deserialize(self, data):
        def deserializeHeper(l):
            if l[0] == "None":
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = deserializeHeper(l)
            root.right = deserializeHeper(l)
            return root
        return deserializeHeper(data.split(','))
