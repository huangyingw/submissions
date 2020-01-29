class Solution:
    def threeSumMulti(self, A, target):
        counts = [0] * 101
        for num in A:
            counts[num] += 1
        result = 0
        for small, small_count in enumerate(counts):
            if small_count == 0:
                continue
            for med, med_count in enumerate(counts[small:], small):
                if med_count == 0:
                    continue
                other = target - small - med
                if other < 0 or other > 100 or counts[other] == 0:
                    continue
                other_count = counts[other]
                if small == med == other:
                    result += small_count * (small_count - 1) * (small_count - 2) / 6
                elif small == med:
                    result += small_count * (small_count - 1) * other_count / 2
                elif other > med:
                    result += small_count * med_count * other_count
        return result % (10 ** 9 + 7)
