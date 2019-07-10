















class Solution:
    def knightDialer(self, N):

        can_reach = [[4, 6],
                     [6, 8],
                     [7, 9],
                     [4, 8],
                     [0, 3, 9],
                     [],
                     [0, 1, 7],
                     [2, 6],
                     [1, 3],
                     [2, 4]]
        counts = [1] * 10
        for _ in range(N - 1):
            new_counts = [0] * 10
            for digit, count in enumerate(counts):
                for next_digit in can_reach[digit]:
                    new_counts[next_digit] += count
            counts = new_counts
        return sum(counts) % (10 ** 9 + 7)
