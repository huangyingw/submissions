











class Solution(object):
    def maxDistToClosest(self, seats):

        empty_seats = []
        max_distance = 0
        last_seat = float("-inf")
        for i, seat in enumerate(seats):
            if seat == 1:
                while empty_seats:
                    seat_i, left_distance = empty_seats.pop()
                    max_distance = max(max_distance, min(left_distance, i - seat_i))
                last_seat = i
            elif i - last_seat > max_distance:
                empty_seats.append((i, i - last_seat))
        while empty_seats:
            seat_i, left_distance = empty_seats.pop()
            max_distance = max(max_distance, left_distance)
        return max_distance
