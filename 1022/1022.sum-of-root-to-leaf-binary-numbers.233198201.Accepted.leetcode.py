class Solution(object):
    def sumRootToLeaf(self, root):
        def traversal(root, paths, pathlen, allpaths):
            if not root:
                return
            if len(paths) > pathlen:
                paths[pathlen] = root.val
            else:
                paths.append(root.val)
            pathlen += 1
            if not root.left and not root.right:
                allpaths.append(int(''.join(str(val) for val in paths[0:pathlen]), 2))
            else:
                traversal(root.left, paths, pathlen, allpaths)
                traversal(root.right, paths, pathlen, allpaths)
        paths = []
        traversal(root, [], 0, paths)
        return sum(paths) % 1000000007
