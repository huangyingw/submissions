_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def exclusiveTime(self, n, logs):

        stack = []
        exclusive = [0 for _ in range(n)]
        start = None
        for log in logs:
            fn, state, time = log.split(":")
            fn, time = int(fn), int(time)
            if state == "start":
                if stack:
                    exclusive[stack[-1]] += time - start
                stack.append(fn)
                start = time
            else:
                exclusive[stack.pop()] += time - start + 1
                start = time + 1
        return exclusive
