class Solution(object):
    def fullJustify(self, words, maxWidth):
        line_chars = 0
        line_words = []
        justified = []
        for word in words:
            if line_chars + len(line_words) + len(word) <= maxWidth:
                line_words.append(word)
                line_chars += len(word)
            else:
                gaps = len(line_words) - 1
                spaces = maxWidth - line_chars
                line = [line_words[0]]
                if gaps == 0:
                    line.append(" " * spaces)
                for line_word in line_words[1:]:
                    space = spaces / gaps
                    if spaces % gaps != 0:
                        space += 1
                    line.append(" " * space)
                    spaces -= space
                    gaps -= 1
                    line.append(line_word)
                justified.append("".join(line))
                line_words = [word]
                line_chars = len(word)
        final_line = " ".join(line_words)
        final_line += " " * (maxWidth - len(final_line))
        justified.append(final_line)
        return justified
