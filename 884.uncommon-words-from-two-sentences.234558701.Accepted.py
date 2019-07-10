


class Solution(object):
    def uncommonFromSentences(self, A, B):

        count = dict()
        result = []
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        for key in count:
            if count[key] == 1:
                result.append(key)
        return result
