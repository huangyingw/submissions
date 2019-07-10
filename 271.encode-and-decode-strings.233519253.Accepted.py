












class Codec:
    def encode(self, strs):

        encoding = []
        for s in strs:
            len_s = str(len(s))
            encoding.append(len_s)
            encoding.append('*')
            encoding.append(s)
        return "".join(encoding)

    def decode(self, s):

        decoding = []
        i = 0
        while i < len(s):
            j = s.find('*', i)
            len_substring = int(s[i:j])
            decoding.append(s[j + 1:j + 1 + len_substring])
            i = j + 1 + len_substring
        return decoding
