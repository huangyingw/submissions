class Solution:
    def bagOfTokensScore(self, tokens, P):
        points, power = 0, P
        left, right = 0, len(tokens) - 1
        tokens.sort()
        while left < len(tokens) and tokens[left] <= power:
            power -= tokens[left]
            points += 1
            left += 1
        if not points:
            return 0
        while right - left > 1:
            points -= 1
            power += tokens[right]
            right -= 1
            while right - left >= 0 and tokens[left] <= power:
                power -= tokens[left]
                points += 1
                left += 1
        return points
