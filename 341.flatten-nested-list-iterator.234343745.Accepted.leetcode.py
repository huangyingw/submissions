class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            curr = self.stack.pop()
            nlist = curr.getList()
            for i in range(len(nlist) - 1, -1, -1):
                self.stack.append(nlist[i])
        return False
