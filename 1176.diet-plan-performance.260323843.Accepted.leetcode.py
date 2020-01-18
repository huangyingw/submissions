class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        calories.append(0)
        window = sum(calories[:k])
        points = 0
        for i in range(k, len(calories)):
            if window < lower:
                points -= 1
            elif window > upper:
                points += 1
            window += calories[i]
            window -= calories[i - k]
        return points
