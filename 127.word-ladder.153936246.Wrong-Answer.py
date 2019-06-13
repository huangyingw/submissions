#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (20.11%)
# Total Accepted:    163.1K
# Total Submissions: 810.9K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string!!!dict is a set type!!!
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.append(end)
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0]
            currlen = curr[1]
            if currword == end:
                return currlen
            for i in range(len(start)):
                part1 = currword[:i]
                part2 = currword[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in dict:
                            q.append((nextword, currlen + 1))
                            dict.remove(nextword)
        return 0
