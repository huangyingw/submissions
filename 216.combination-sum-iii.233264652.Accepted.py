_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def combinationSum3(self, k, n):

        results = []
        self.cs3([], n, results, k)
        return results

    def cs3(self, partial, target, results, k):
        if len(partial) == k and target == 0:
            results.append(partial)
        if len(partial) >= k or target <= 0:
            return
        last_used = 0 if not partial else partial[-1]
        for i in range(last_used + 1, 10):
            self.cs3(partial + [i], target - i, results, k)
