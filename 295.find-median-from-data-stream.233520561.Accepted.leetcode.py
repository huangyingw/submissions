import heapq


class MedianFinder:
    def __init__(self):
        self.lower = []
        self.higher = []

    def addNum(self, num):
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)
        if len(self.higher) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.higher))
        elif len(self.lower) > 1 + len(self.higher):
            heapq.heappush(self.higher, -heapq.heappop(self.lower))

    def findMedian(self):
        if len(self.lower) > len(self.higher):
            return float(-self.lower[0])
        return (-self.lower[0] + self.higher[0]) // 2.0
