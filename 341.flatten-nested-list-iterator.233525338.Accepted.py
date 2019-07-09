_author_ = 'jake'
_project_ = 'leetcode'
































class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flat = []

        def flatten(nested):
            for n in nested:
                if n.isInteger():
                    self.flat.append(n.getInteger())
                else:
                    flatten(n.getList())
        flatten(nestedList)
        self.flat = self.flat[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.flat.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.flat)
