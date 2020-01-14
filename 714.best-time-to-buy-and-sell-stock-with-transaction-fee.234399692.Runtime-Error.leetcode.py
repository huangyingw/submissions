class Solution1:
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
class Solution2:
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
        profit = 0
        buy = prices[0]
        for x in prices:
            if x < buy:
                buy = x
            elif x > fee + buy:
                profit = profit + x - buy - fee
                buy = x - fee
        return profit
