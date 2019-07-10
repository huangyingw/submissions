

















from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):

        n = len(senate)
        d, r = deque(), deque()
        for i, c in enumerate(senate):
            if c == "D":
                d.append(i)
            else:
                r.append(i)
        while d and r:
            d_senator = d.popleft()
            r_senator = r.popleft()
            if d_senator < r_senator:
                d.append(d_senator + n)
            else:
                r.append(r_senator + n)
        return "Radiant" if r else "Dire"
