import bisect


class MyCalendar(object):
    def __init__(self):
        self.bookings = [(float("-inf"), float("-inf")), (float("inf"), float("inf"))]

    def book(self, start, end):
        i = bisect.bisect_left(self.bookings, (start, end))
        if end > self.bookings[i][0]:
            return False
        if start < self.bookings[i - 1][1]:
            return False
        self.bookings.insert(i, (start, end))
        return True
