_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def flipgame(self, fronts, backs):

        duplicates = {f for f, b in zip(fronts, backs) if f == b}
        result = float("inf")
        for f, b in zip(fronts, backs):
            if f != b:
                if f not in duplicates:
                    result = min(result, f)
                if b not in duplicates:
                    result = min(result, b)
        return 0 if result == float("inf") else result
