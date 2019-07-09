_author_ = 'jake'
_project_ = 'leetcode'















from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks)
        max_count = max(counts.values())
        result = (max_count - 1) * (n + 1)
        for count in counts.values():
            if count == max_count:
                result += 1
        return max(result, len(tasks))
