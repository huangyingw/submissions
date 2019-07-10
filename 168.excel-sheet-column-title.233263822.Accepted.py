





from collections import deque


class Solution(object):
    def convertToTitle(self, n):

        column = deque()
        while n > 0:
            n, output = divmod(n - 1, 26)
            column.appendleft(output)
        return "".join([chr(i + ord('A')) for i in column])
