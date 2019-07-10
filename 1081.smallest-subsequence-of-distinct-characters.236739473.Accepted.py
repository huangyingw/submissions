class Solution(object):
    def smallestSubsequence(self, text):

        if not text:
            return ''
        import collections
        freq_map = collections.Counter(text)
        used = [False] * 26
        result = ''
        for char in text:
            freq_map[char] -= 1
            if used[ord(char) - 97]:
                continue
            while (result and result[-1] > char and freq_map[result[-1]] > 0):
                used[ord(result[-1]) - 97] = False
                result = result[:-1]
            used[ord(char) - 97] = True
            result += char
        return result
