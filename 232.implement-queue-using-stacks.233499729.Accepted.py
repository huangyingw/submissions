_author_ = 'jake'
_project_ = 'leetcode'













class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reversed = []
        self.top = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.top = x
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.reversed:
            while self.stack:
                self.reversed.append(self.stack.pop())
        return self.reversed.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.reversed:
            return self.reversed[-1]
        return self.top

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack and not self.reversed
