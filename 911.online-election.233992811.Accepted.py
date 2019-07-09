_author_ = 'jake'
_project_ = 'leetcode'













from collections import defaultdict
import bisect


class TopVotedCandidate:
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.leader = []
        counts = defaultdict(int)
        max_count = 0
        for person, time in zip(persons, times):
            counts[person] += 1
            if counts[person] > max_count:
                max_count += 1
                leaders = [person]
            elif counts[person] == max_count:
                leaders.append(person)
            self.leader.append(leaders[-1])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i = bisect.bisect_left(self.times, t)
        if i == len(self.times) or self.times[i] > t:
            return self.leader[i - 1]
        return self.leader[i]
