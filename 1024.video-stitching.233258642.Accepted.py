_project_ = 'leetcode'




















class Solution(object):
    def videoStitching(self, clips, T):

        prev_stitch_end, stitch_end = -1, 0
        result = 0
        for start, end in sorted(clips):
            if start > stitch_end or stitch_end >= T:
                break
            if start > prev_stitch_end:
                result += 1
                prev_stitch_end = stitch_end
            stitch_end = max(stitch_end, end)
        return -1 if stitch_end < T else result
