













class Solution(object):
    def getMoneyAmount(self, n):




        min_money = [[0 for _ in range(n)], [i for i in range(1, n)]]
        for range_length in range(3, n + 1):
            min_money.append([])
            for lower in range(1, n + 2 - range_length):
                upper = lower + range_length - 1
                min_cost = float('inf')
                for guess in range((lower + upper) // 2, upper):
                    cost = guess + max(min_money[guess - lower - 1][lower - 1], min_money[upper - guess - 1][guess])
                    min_cost = min(min_cost, cost)
                min_money[-1].append(min_cost)
        return min_money[n - 1][0]
