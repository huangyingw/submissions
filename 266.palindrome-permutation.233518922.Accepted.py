_author_ = 'jake'
_project_ = 'leetcode'





from collections import Counter


class Solution(object):
    def canPermutePalindrome(self, s):

        freq = Counter(s)
        odd = False
        for letter, count in freq.items():
            if count % 2 == 1:
                if odd:
                    return False
                odd = True
        return True
