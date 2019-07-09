_author_ = 'jake'
_project_ = 'leetcode'










from collections import defaultdict, Counter


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        freq = Counter(A)
        pairs = defaultdict(set)
        unique = list(freq.keys())
        pairs[None] = unique
        for i, num1 in enumerate(unique):
            for num2 in unique[i:]:
                if int((num1 + num2) ** 0.5) ** 2 == num1 + num2:
                    pairs[num1].add(num2)
                    pairs[num2].add(num1)

        def helper(num, length):
            if length == len(A):
                return 1
            count = 0
            for next_num in pairs[num]:
                if freq[next_num] > 0:
                    freq[next_num] -= 1
                    count += helper(next_num, length + 1)
                    freq[next_num] += 1
            return count
        return helper(None, 0)
