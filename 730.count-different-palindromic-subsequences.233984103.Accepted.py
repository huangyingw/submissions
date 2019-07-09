_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        NUM_LETTERS, MOD = 4, 10 ** 9 + 7
        S = [ord(c) - ord("a") for c in S]
        memo = {}
        last_indices = [-1 for _ in range(NUM_LETTERS)]
        prev_index_letter = [None for _ in
                             range(len(S))]
        for i in range(len(S)):
            last_indices[S[i]] = i
            prev_index_letter[i] = last_indices[:]
        last_indices = [-1 for _ in range(NUM_LETTERS)]
        next_index_letter = [None for _ in range(len(S))]
        for i in range(len(S) - 1, -1, -1):
            last_indices[S[i]] = i
            next_index_letter[i] = last_indices[:]

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            count = 1
            for letter in range(4):
                next_index = next_index_letter[i][letter]
                prev_index = prev_index_letter[j][letter]
                if i <= next_index <= j:
                    count += 1
                if next_index != -1 and prev_index != -1 and prev_index > next_index:
                    count += helper(next_index + 1, prev_index - 1)
            count %= MOD
            memo[(i, j)] = count
            return count
        return helper(0, len(S) - 1) - 1
