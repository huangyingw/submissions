class Node(object):
    def __init__(self, value):
        self.children = {}
        self.value = value


class FileSystem(object):
    def __init__(self):
        self.root = Node(None)

    def traverse(self, folders):
        node = self.root
        for folder in folders[1:]:
            if folder not in node.children:
                return None
            node = node.children[folder]
        return node

    def createPath(self, path, value):
        folders = path.split("/")
        node = self.traverse(folders[:-1])
        if node is None or folders[-1] in node.children:
            return False
        node.children[folders[-1]] = Node(value)
        return True

    def get(self, path):
        node = self.traverse(path.split("/"))
        if not node:
            return -1
        return node.value
