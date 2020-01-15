class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
