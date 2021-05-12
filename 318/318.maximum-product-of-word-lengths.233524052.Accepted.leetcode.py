class Solution(object):
    def maxProduct(self, words):
        codes = []
        for word in words:
            codes.append(sum(1 << (ord(c) - ord('a')) for c in set(word)))
        max_product = 0
        for i in range(len(codes) - 1):
            for j in range(i + 1, len(codes)):
                if not (codes[i] & codes[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product
