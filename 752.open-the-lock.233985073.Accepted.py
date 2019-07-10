_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def openLock(self, deadends, target):

        queue, target = {"0000"}, {target}
        visited = set()
        deadends = set(deadends)
        steps = 0

        def shift(combo):
            shifts = set()
            for i, c in enumerate(combo):
                shifted = (int(c) + 1) % 10
                shifts.add(combo[:i] + str(shifted) + combo[i + 1:])
                shifted = (int(c) - 1) % 10
                shifts.add(combo[:i] + str(shifted) + combo[i + 1:])
            return shifts
        while queue:
            if target & queue:
                return steps
            new_queue = set()
            steps += 1
            for combo in queue:
                if combo in visited or combo in deadends:
                    continue
                visited.add(combo)
                new_queue |= shift(combo)
            queue, target = target, new_queue
        return -1
