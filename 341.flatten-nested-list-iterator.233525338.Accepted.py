































class NestedIterator(object):
    def __init__(self, nestedList):

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

        return self.flat.pop()

    def hasNext(self):

        return bool(self.flat)
