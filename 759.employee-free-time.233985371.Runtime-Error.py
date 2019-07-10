










import heapq



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def employeeFreeTime(self, schedule):

        employees = len(schedule)
        next_start_times = [(schedule[i][0].start, 0, i) for i in range(employees)]
        heapq.heapify(next_start_times)
        last_end_time = next_start_times[0][0]
        result = []
        while next_start_times:
            interval_start_time, interval, employee = heapq.heappop(next_start_times)
            if interval + 1 < len(schedule[employee]):
                heapq.heappush(next_start_times, (schedule[employee][interval + 1].start, interval + 1, employee))
            if interval_start_time > last_end_time:
                result.append(Interval(last_end_time, interval_start_time))
            last_end_time = max(last_end_time, schedule[employee][interval].end)
        return result
