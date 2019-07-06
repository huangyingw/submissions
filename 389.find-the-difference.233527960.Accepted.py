_author_ = 'jake'
_project_ = 'leetcode'
# https://leetcode.com/problems/find-the-difference/
# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.
# Count frequencies of letters in s. For each letter in t, decrement count. If any letter count is negative then it
# is the additional letter in t.
# Time - O(n)
# Space - O(1)


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = [0 for _ in range(26)]
        for c in s:
            counts[ord(c) - ord("a")] += 1
        for c in t:
            index = ord(c) - ord("a")
            counts[index] -= 1
            if counts[index] < 0:
                return c
