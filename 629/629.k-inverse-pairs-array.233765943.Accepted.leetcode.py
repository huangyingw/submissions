class Solution(object):
    def kInversePairs(self, n, k):
        if k == 0:
            return 1
        MODULO = 10 ** 9 + 7
        inverse_pairs = [0 for _ in range(k + 1)]
        for num in range(1, n + 1):
            next_inverse_pairs = [1]
            for nb_pairs in range(1, k + 1):
                next_inverse_pairs.append(next_inverse_pairs[-1])
                next_inverse_pairs[-1] += inverse_pairs[nb_pairs]
                if nb_pairs - num >= 0:
                    next_inverse_pairs[-1] -= inverse_pairs[nb_pairs - num]
                next_inverse_pairs[-1] %= MODULO
            inverse_pairs = next_inverse_pairs
        return (inverse_pairs[-1] - inverse_pairs[-2]) % MODULO
