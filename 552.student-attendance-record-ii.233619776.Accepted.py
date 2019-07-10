














class Solution(object):
    def checkRecord(self, n):

        BASE = 10 ** 9 + 7
        records = [1, 2]
        zero, one, two = 1, 1, 0



        for _ in range(2, n + 1):
            zero, one, two = (zero + one + two) % BASE, zero, one
            records.append((zero + one + two) % BASE)

        result = records[-1]

        for i in range(n):
            result += records[i] * records[n - 1 - i]
            result %= BASE
        return result
