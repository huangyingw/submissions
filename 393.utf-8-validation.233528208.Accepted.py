_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def validUtf8(self, data):

        i = 0
        while i < len(data):
            byte = data[i]
            if byte & (1 << 7) == 0:
                i += 1
                continue
            bit = 6
            while byte & (1 << bit) and bit > 3:
                bit -= 1
            if byte & (1 << bit) or bit == 6:
                return False
            bytes = 6 - bit
            i += 1
            while bytes:
                if i >= len(data) or data[i] & (128 + 64) != 128:
                    return False
                bytes -= 1
                i += 1
        return True
