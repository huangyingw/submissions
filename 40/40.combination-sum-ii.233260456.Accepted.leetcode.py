from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):

        results = []
        freq = list(Counter(candidates).items())
        self.combos(freq, 0, target, [], results)
        return results

    def combos(self, freq, next, target, partial, results):
        if target == 0:
            results.append(partial)
            return
        if next == len(freq):
            return
        for i in range(freq[next][1] + 1):
            if i * freq[next][0] > target:
                break
            self.combos(freq, next + 1, target - i * freq[next][0], partial + [freq[next][0]] * i, results)


class Solution_Iterative(object):
    def combinationSum2(self, candidates, target):
        results = []
        partials = [[]]
        freq = list(Counter(candidates).items())
        for candidate, count in freq:
            new_partials = []
            for partial in partials:
                partial_sum = sum(partial)
                for i in range(count + 1):
                    if partial_sum + candidate * i < target:
                        new_partials.append(partial + [candidate] * i)
                    elif partial_sum + candidate * i == target:
                        results.append(partial + [candidate] * i)
                    if partial_sum + candidate * i >= target:
                        break
            partials = new_partials
        return results
