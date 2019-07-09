_author_ = 'jake'
_project_ = 'leetcode'








class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.front = None
        self.it = iterator
        if self.it.hasNext():
            self.front = self.it.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.front

    def next(self):
        """
        :rtype: int
        """
        temp = self.front
        self.front = None
        if self.it.hasNext():
            self.front = self.it.next()
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.front)
