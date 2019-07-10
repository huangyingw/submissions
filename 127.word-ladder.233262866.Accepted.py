_author_ = 'jake'
_project_ = 'leetcode'














from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        length = 1
        visited = set()
        if endWord not in wordList:
            return 0
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '_' + word[i + 1:]
                graph[wildcard].add(word)
        front, back = {beginWord}, {endWord}
        while front:
            if front & back:
                return length
            new_front = set()
            for word in front:
                visited.add(word)
                for i in range(len(word)):
                    next_words = graph[word[:i] + '_' + word[i + 1:]]
                    next_words -= visited
                    new_front |= next_words
            length += 1
            front = new_front
            if len(back) < len(front):
                front, back = back, front
        return 0
