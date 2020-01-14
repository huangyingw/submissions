class Solution(object):
    def removeSubfolders(self, folder):
        paths = [f.split("/") for f in folder]
        paths.sort(key=len)
        result = []
        root = {}
        for i, path in enumerate(paths):
            node = root
            for level in path[1:]:
                if level not in node:
                    node[level] = {}
                node = node[level]
                if "TERMINAL" in node:
                    break
            else:
                node["TERMINAL"] = {}
                result.append("/".join(path))
        return result
