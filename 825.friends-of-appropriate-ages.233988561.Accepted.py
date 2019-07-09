_author_ = 'jake'
_project_ = 'leetcode'













from collections import Counter


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        freq = Counter(ages)
        age_counts = [(k, v) for k, v in freq.items()]
        age_counts.sort()
        requests = 0
        for a, (age_a, count_a) in enumerate(age_counts):
            for age_b, count_b in age_counts[:a]:
                if age_b > 0.5 * age_a + 7 and (age_b < 100 or age_a > 100):
                    requests += count_a * count_b
            if age_a > 14:
                requests += count_a * (count_a - 1)
        return requests
