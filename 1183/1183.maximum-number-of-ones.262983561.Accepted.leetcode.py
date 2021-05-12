class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        whole_width, remainder_width = divmod(width, sideLength)
        whole_height, remainder_height = divmod(height, sideLength)
        matrix = []
        for r in range(sideLength):
            for c in range(sideLength):
                repeats = (whole_width + int(r < remainder_width)) * (whole_height + int(c < remainder_height))
                matrix.append(repeats)
        return sum(sorted(matrix, reverse=True)[:maxOnes])
