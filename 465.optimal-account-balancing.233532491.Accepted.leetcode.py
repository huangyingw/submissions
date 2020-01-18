from collections import defaultdict


class Solution(object):
    def minTransfers(self, transactions):
        balances = defaultdict(int)
        for lender, receiver, amount in transactions:
            balances[lender] += amount
            balances[receiver] -= amount
        net_balances = [b for b in balances.values() if b != 0]

        def transfers(net_balances):
            if not net_balances:
                return 0
            b = net_balances[0]
            for i in range(1, len(net_balances)):
                if b == -net_balances[i]:
                    return 1 + transfers(net_balances[1:i] + net_balances[i + 1:])
            min_transfers = float("inf")
            for i in range(1, len(net_balances)):
                if b * net_balances[i] < 0:
                    count = 1 + transfers(net_balances[1:i] + net_balances[i + 1:] + [b + net_balances[i]])
                    min_transfers = min(min_transfers, count)
            return min_transfers
        return transfers(net_balances)
