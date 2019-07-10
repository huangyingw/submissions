_author_ = 'jake'
_project_ = 'leetcode'









from collections import defaultdict


class Solution(object):
    def reconstructQueue(self, people):

        queue = []
        height_groups = defaultdict(list)
        for height, in_front in people:
            height_groups[height].append(in_front)
        all_heights = list(height_groups.keys())
        all_heights.sort(reverse=True)
        for height in all_heights:
            height_groups[height].sort()
            for in_front in height_groups[height]:
                queue.insert(in_front, [height, in_front])
        return queue
