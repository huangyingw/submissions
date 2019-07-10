














class Solution(object):
    def uniqueLetterString(self, S):

        unique = 0
        indices = [[-1] for _ in range(26)]
        for i, c in enumerate(S):
            indices[ord(c) - ord("A")].append(i)
        for index_list in indices:
            index_list.append(len(S))
            for i in range(1, len(index_list) - 1):
                unique += (index_list[i] - index_list[i - 1]) * (index_list[i + 1] - index_list[i])
        return unique % (10 ** 9 + 7)
