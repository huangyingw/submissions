class Solution(object):
    def corpFlightBookings(self, bookings, n):
        result = [0] * (n + 1)
        for start, end, seats in bookings:
            result[start - 1] += seats
            result[end] -= seats
        seats = 0
        for i, change in enumerate(result):
            seats += change
            result[i] = seats
        return result[:-1]
