class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(5))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-5:]]


class Codec_counter:
    def __init__(self):
        self.code2url = {}
        self.url2code = {}
        self.count = 0

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            self.count += 1
            self.code2url[str(self.count)] = longUrl
            self.url2code[longUrl] = str(self.count)
        return "http://tinyurl.com/" + str(self.count)

    def decode(self, shortUrl):
        return self.code2url[shortUrl.split('/')[-1]]
import uuid


class Codec_uuid3:
    def __init__(self):
        self.code2url = {}

    def encode(self, longUrl):
        code = uuid.uuid3(uuid.NAMESPACE_URL, str(longUrl))
        self.code2url[str(code)] = longUrl
        return "http://tinyurl.com/" + str(code)

    def decode(self, shortUrl):
        return self.code2url[shortUrl.split('/')[-1]]
import uuid


class Codec_uuid4:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __init__(self):
        self.code2url = {}

    def encode(self, longUrl):
        code = uuid.uuid4()
        self.code2url[str(code)] = longUrl
        return "http://tinyurl.com/" + str(code)

    def decode(self, shortUrl):
        return self.code2url[shortUrl.split('/')[-1]]
