class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        K += 1
        left, right = 1, sum(sweetness) / K

        def can_split(x):
            piece, count = 0, 0
            for sweet in sweetness:
                piece += sweet
                if piece >= x:
                    count += 1
                    piece = 0
            return count >= K
        while left < right:
            mid = (left + right + 1) / 2
            if can_split(mid):
                left = mid
            else:
                right = mid - 1
        return left
