



class Codec:
    def encode(self, longUrl):

        self.hash = {}
        if longUrl not in self.hash:
            idx = hash(longUrl)
            self.hash[idx] = longUrl
        final_string = 'https://tinyurl.com/' + str(idx)
        return (final_string)

    def decode(self, shortUrl):

        v = shortUrl[20:len(shortUrl)]
        return (self.hash[int(v)])
