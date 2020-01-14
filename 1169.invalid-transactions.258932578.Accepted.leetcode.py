from collections import defaultdict
class Solution(object):
    def invalidTransactions(self, transactions):
        elements = [transaction.split(",") + [i] for i, transaction in enumerate(transactions)]
        elements.sort(key=lambda x: int(x[1]))
        user_transactions = defaultdict(list)
        invalid = set()
        for transaction in elements:
            name, time, cost, city, i = transaction
            time = int(time)
            if int(cost) > 1000:
                invalid.add(transactions[i])
            j = len(user_transactions[name]) - 1
            while j >= 0 and time - user_transactions[name][j][0] <= 60:
                if user_transactions[name][j][1] != city:
                    invalid.add(transactions[i])
                    invalid.add(transactions[user_transactions[name][j][2]])
                j -= 1
            user_transactions[name].append([time, city, i])
        return list(invalid)
