class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        base_satisfied = 0
        window, best_window = 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                window += customers[i]
            else:
                base_satisfied += customers[i]
            if i - X >= 0 and grumpy[i - X] == 1:
                window -= customers[i - X]
            best_window = max(best_window, window)
        return base_satisfied + best_window
