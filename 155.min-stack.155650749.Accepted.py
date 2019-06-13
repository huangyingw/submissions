class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.min or self.min[-1] >= x:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.data.pop()
        if temp == self.min[-1]:
            self.min.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
