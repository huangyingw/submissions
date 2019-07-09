_author_ = 'jake'
_project_ = 'leetcode'












import bisect


class ExamRoom(object):
    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = []
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        if not self.seats:
            self.seats.append(0)
            return 0
        max_dist, index = self.seats[0], 0
        for i in range(len(self.seats) - 1):
            dist = (self.seats[i + 1] - self.seats[i]) // 2
            if dist > max_dist:
                max_dist = dist
                index = self.seats[i] + dist
        if self.N - 1 - self.seats[-1] > max_dist:
            index = self.N - 1
        bisect.insort(self.seats, index)
        return index

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seats.remove(p)
