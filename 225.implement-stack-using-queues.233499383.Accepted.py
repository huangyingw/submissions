_author_ = 'jake'
_project_ = 'leetcode'
















from collections import deque


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.appendleft(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        new_queue = deque()
        while True:
            x = self.queue.pop()
            if not self.queue:
                self.queue = new_queue
                return x
            new_queue.appendleft(x)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        new_queue = deque()
        while self.queue:
            x = self.queue.pop()
            new_queue.appendleft(x)
        self.queue = new_queue
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
