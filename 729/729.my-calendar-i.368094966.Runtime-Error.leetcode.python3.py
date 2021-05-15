from bisect import bisect


class MyCalendar1(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True


class MyCalendar2:
    def __init__(self):
        self.eventList = [(0, 0), (float('inf'), float('inf'))]

    def book(self, start, end):
        p = bisect(self.eventList, (start, end))
        if self.eventList[p - 1][1] > start:
            return False
        if self.eventList[p][0] < end:
            return False
        self.eventList.insert(p, (start, end))
        return True
