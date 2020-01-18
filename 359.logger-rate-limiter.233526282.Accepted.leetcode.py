class Logger(object):
    def __init__(self):
        self.last = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.last or timestamp - self.last[message] >= 10:
            self.last[message] = timestamp
            return True
        return False
