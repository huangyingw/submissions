class Solution(object):
    def longestDecomposition(self, text):
        n = len(text)
        start_prefix = 0
        result = 0
        while start_prefix <= (n - 1) // 2:
            for length in range(1, ((n - 2 * start_prefix) // 2) + 1):
                prefix = text[start_prefix:start_prefix + length]
                suffix = text[n - start_prefix - length:n - start_prefix]
                if prefix == suffix:
                    result += 2
                    start_prefix += length
                    break
            else:
                result += 1
                break
        return result
