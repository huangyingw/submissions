_author_ = 'jake'
_project_ = 'leetcode'















from collections import defaultdict
import string


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return []
        wordList = set(wordList)
        left, right = {beginWord}, {endWord}
        left_parents, right_parents = defaultdict(set), defaultdict(set)
        swapped = False
        while left and right and not (left & right):
            if len(right) < len(left):
                left, right = right, left
                left_parents, right_parents = right_parents, left_parents
                swapped = not swapped
            next_left = defaultdict(set)
            for word in left:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = word[:i] + char + word[i + 1:]
                        if n in wordList and n not in left_parents:
                            next_left[n].add(word)
            left_parents.update(next_left)
            left = set(next_left.keys())
        if swapped:
            left, right = right, left
            left_parents, right_parents = right_parents, left_parents
        ladders = [[word] for word in left & right]
        while ladders and ladders[0][0] not in beginWord:
            ladders = [[p] + l for l in ladders for p in left_parents[l[0]]]
        while ladders and ladders[0][-1] != endWord:
            ladders = [l + [p] for l in ladders for p in right_parents[l[-1]]]
        return ladders
