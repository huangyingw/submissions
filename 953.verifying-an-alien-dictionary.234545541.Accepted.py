




class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {v: i for i, v in enumerate(order)}
        encode_words = []



        encode_words = [[d[l] for l in word] for word in words]
        return sorted(encode_words) == encode_words
if __name__ == '__main__':
    t = Solution()
