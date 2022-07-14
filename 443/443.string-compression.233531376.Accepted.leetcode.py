class Solution(object):
    def compress(self, chars):

        chars += " "
        char_start = 0
        result_length = 0
        for i, c in enumerate(chars):
            if c != chars[char_start]:
                chars[result_length] = chars[char_start]
                result_length += 1
                seq_length = i - char_start
                if seq_length > 1:
                    digits = list(str(seq_length))
                    digits_length = len(digits)
                    chars[result_length:result_length + digits_length] = digits
                    result_length += digits_length
                char_start = i
        return result_length
