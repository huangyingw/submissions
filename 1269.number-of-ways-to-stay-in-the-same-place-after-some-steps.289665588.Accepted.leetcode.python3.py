class Solution(object):
    def numWays(self, steps, arrLen):
        i_to_count = [1]
        for step in range(steps):
            new_i_to_count = [0] * (len(i_to_count) + 1)
            for i, count in enumerate(i_to_count[:steps - step + 1]):
                if i + 1 < arrLen:
                    new_i_to_count[i + 1] += count
                new_i_to_count[i] += count
                if i - 1 >= 0:
                    new_i_to_count[i - 1] += count
            i_to_count = new_i_to_count
        return i_to_count[0] % (10 ** 9 + 7)
