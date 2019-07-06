class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(endWord)
        queue = [beginWord]
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if word == endWord:
                    return depth
                for i in range(len(beginWord)):
                    alphabets = string.ascii_lowercase
                    for c in alphabets:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordList:
                            queue.append(newWord)
                            wordList.remove(newWord)
        return 0
