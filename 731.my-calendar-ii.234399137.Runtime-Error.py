



class MyCalendarTwo1:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
import bisect


class MyCalendarTwo2:
    def __init__(self):


        self.cal = [0]
        self.bookings = [0]

    def book(self, start, end):
        i = bisect.bisect(self.cal, start)
        j = bisect.bisect_left(self.cal, end)
        if 2 in self.bookings[i - 1:j]:
            return False
        else:
            if start == self.cal[i - 1]:
                self.bookings[i - 1] += 1
            else:
                self.bookings[i:i] = [self.bookings[i - 1]]
                self.cal[i:i] = [start]
                j += 1
            for cnt in range(i, j):
                self.bookings[cnt] += 1
            if j == len(self.cal) or end != self.cal[j]:
                self.bookings[j:j] = [self.bookings[j - 1] - 1]
                self.cal[j:j] = [end]
            return True
