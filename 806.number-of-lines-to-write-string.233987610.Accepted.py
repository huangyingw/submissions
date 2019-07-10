class Solution(object):
    def numberOfLines(self, widths, S):
        line, width = 0, 100
        for c in S:
            c_length = widths[ord(c) - ord("a")]
            if width + c_length > 100:
                line += 1
                width = 0
            width += c_length
        return [line, width]
