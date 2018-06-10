class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        queue = [(beginWord, 1)]

        while queue:
            e, lens = queue.pop(0)

            if e == endWord:
                return lens

            for i in range(len(e)):
                left = e[:i]
                right = e[i + 1:]

                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if e[i] != c:
                        nextWord = left + c + right

                        if nextWord in wordList:
                            queue.append((nextWord, lens + 1))
                            wordList.remove(nextWord)

        return 0
