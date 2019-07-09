_author_ = 'jake'
_project_ = 'leetcode'














class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [(float("-inf"), float("-inf"))]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: int
        """
        x, _ = self.stack.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        x, target = self.stack.pop()
        while x != target:
            temp.append(x)
            x, _ = self.stack.pop()
        for x in reversed(temp):
            self.push(x)
        return target
