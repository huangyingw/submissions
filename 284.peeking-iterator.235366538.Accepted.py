_author_ = 'jake'
_project_ = 'leetcode'








class PeekingIterator(object):
    def __init__(self, iterator):

        self.front = None
        self.it = iterator
        if self.it.hasNext():
            self.front = self.it.next()

    def peek(self):

        return self.front

    def next(self):

        temp = self.front
        self.front = None
        if self.it.hasNext():
            self.front = self.it.next()
        return temp

    def hasNext(self):

        return bool(self.front)
