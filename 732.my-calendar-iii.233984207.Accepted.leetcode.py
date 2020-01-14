import bisect
class MyCalendarThree(object):
    def __init__(self):
        self.bookings = [[float("-inf"), 0], [float("inf"), 0]]
        self.max_booking = 0
    def book(self, start, end):
        i = bisect.bisect_left(self.bookings, [start, -1])
        if self.bookings[i][0] != start:
            count = self.bookings[i - 1][1]
            self.bookings.insert(i, [start, count + 1])
            self.max_booking = max(self.max_booking, count + 1)
            i += 1
        while end > self.bookings[i][0]:
            self.bookings[i][1] += 1
            self.max_booking = max(self.max_booking, self.bookings[i][1])
            i += 1
        if self.bookings[i][0] != end:
            count = self.bookings[i - 1][1]
            self.bookings.insert(i, [end, count - 1])
        return self.max_booking
