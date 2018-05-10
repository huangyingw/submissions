#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (27.12%)
# Total Accepted:    224.7K
# Total Submissions: 828.5K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if 'a' <= s[start] <= 'z' or 'a' <= s[end] <= 'z':
                if s[start] != s[end]:
                    return False
            if not 'a' <= s[start] <= 'z':
                start += 1
            elif not 'a' <= s[end] <= 'z':
                end -= 1
            elif s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
