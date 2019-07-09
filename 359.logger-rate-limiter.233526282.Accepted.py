_author_ = 'jake'
_project_ = 'leetcode'












class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.last or timestamp - self.last[message] >= 10:
            self.last[message] = timestamp
            return True
        return False
