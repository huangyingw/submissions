_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        max_profits = list(zip(difficulty, profit))
        max_profits.sort()
        max_profits.append((float("inf"), 0))
        total_profit = 0
        best_profit = 0
        i = 0
        worker.sort()
        for diff in worker:
            while max_profits[i][0] <= diff:
                best_profit = max(best_profit, max_profits[i][1])
                i += 1
            total_profit += best_profit
        return total_profit
