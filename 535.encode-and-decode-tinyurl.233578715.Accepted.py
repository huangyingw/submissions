_author_ = 'jake'
_project_ = 'leetcode'









import random


class Codec:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __init__(self):
        self.map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        encoding = []
        for i in range(6):
            encoding.append(self.letters[random.randint(0, 61)])
        encoding = "".join(encoding)
        if encoding in self.map:
            encoding = self.encode(longUrl)
        self.map[encoding] = longUrl
        return encoding

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl]
