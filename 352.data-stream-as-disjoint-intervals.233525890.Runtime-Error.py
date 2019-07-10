




















class IntervalNode(object):
    def __init__(self, interval):
        self.inner = interval
        self.parent = self


class SummaryRanges(object):
    def __init__(self):

        self.parents = {}
        self.intervals = set()

    def get_parent(self, v):
        if v not in self.parents:
            return None
        interval_node = self.parents[v]
        while interval_node != interval_node.parent:
            interval_node.parent = interval_node.parent.parent
            interval_node = interval_node.parent
        return interval_node

    def addNum(self, val):

        if val in self.parents:
            return
        lower = self.get_parent(val - 1)
        upper = self.get_parent(val + 1)
        if lower and upper:
            lower.inner.end = upper.inner.end
            self.parents[val] = lower
            upper.parent = lower
            self.intervals.remove(upper.inner)
        elif lower:
            lower.inner.end += 1
            self.parents[val] = lower
        elif upper:
            upper.inner.start -= 1
            self.parents[val] = upper
        else:
            new_inner = Interval(val, val)
            self.parents[val] = IntervalNode(new_inner)
            self.intervals.add(new_inner)

    def getIntervals(self):

        result = list(self.intervals)
        result.sort(key=lambda x: x.start)
        return result
