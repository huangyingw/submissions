class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        word_freq = [0] * 12
        for word in words:
            word_freq[word.count(min(word))] += 1
        for i in range(10, 0, -1):
            word_freq[i] += word_freq[i + 1]
        return [word_freq[query.count(min(query)) + 1] for query in queries]
