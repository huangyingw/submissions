_author_ = 'jake'
_project_ = 'leetcode'

















class MyCalendarTwo(object):
    def __init__(self):
        self.doubles = []
        self.intervals = []

    def book(self, start, end):

        for i, j in self.doubles:
            if start < j and end > i:
                return False
        for i, j in self.intervals:
            if start < j and end > i:
                self.doubles.append((max(start, i), min(end, j)))
        self.intervals.append((start, end))
        return True
