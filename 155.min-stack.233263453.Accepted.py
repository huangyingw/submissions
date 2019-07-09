_author_ = 'jake'
_project_ = 'leetcode'












class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.main.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: void
        """
        item = self.main.pop()
        if item == self.mins[-1]:
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
