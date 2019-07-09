_author_ = 'jake'
_project_ = 'leetcode'



















class Folder(object):
    def __init__(self):
        self.children = {}


class FileSystem(object):
    def __init__(self):
        self.root = Folder()
        self.files = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        path = path.split("/")
        if path[-1] in self.files:
            return [path[-1]]
        folder = self.root
        if path[-1] != "":
            for folder_string in path[1:]:
                folder = folder.children[folder_string]
        return sorted(list(folder.children.keys()))

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        folder = self.root
        for folder_string in path.split("/")[1:]:
            if folder_string not in folder.children:
                folder.children[folder_string] = Folder()
            folder = folder.children[folder_string]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        path = filePath.split("/")
        file_name = path[-1]
        if file_name in self.files:
            self.files[file_name] += content
        else:
            self.files[file_name] = content
            folder = self.root
            for folder_string in path[1:-1]:
                folder = folder.children[folder_string]
            folder.children[file_name] = None

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        file_name = filePath.split("/")[-1]
        return self.files[file_name]
