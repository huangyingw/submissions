_author_ = 'jake'
_project_ = 'leetcode'


















class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        digits = len(n)
        candidates = {int("1" + "0" * (digits - 1) + "1")}
        if len(n) > 1:
            candidates.add(int("9" * (digits - 1)))
        mid = len(n) // 2
        left = n[:mid]
        if len(n) % 2 == 1:
            centre_count = 1
            centre = n[mid]
            right = left[::-1]
        else:
            centre_count = 2
            centre = left[-1]
            left = left[:-1]
            right = left[::-1]
        candidates.add(int(left + centre * centre_count + right))
        if centre != "9":
            new_centre = str(int(centre) + 1)
            candidates.add(int(left + new_centre * centre_count + right))
        if centre != "0":
            new_centre = str(int(centre) - 1)
            candidates.add(int(left + new_centre * centre_count + right))
        n_int = int(n)
        candidates.discard(n_int)
        candidates = list(candidates)
        candidates.sort(key=lambda x: (abs(x - n_int), x))
        return str(candidates[0])
