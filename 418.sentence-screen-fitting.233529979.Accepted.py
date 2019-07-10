











class Solution(object):
    def wordsTyping(self, sentence, rows, cols):

        sentence_len = sum(len(w) for w in sentence) + len(sentence)

        line_fits = []
        for start_word_index in range(len(sentence)):
            row_length, sentences = 0, 0
            word_index = start_word_index
            while row_length + sentence_len <= cols:
                row_length += sentence_len
                sentences += 1
            while row_length + len(sentence[word_index]) <= cols:
                row_length += len(sentence[word_index]) + 1
                word_index += 1
                if word_index == len(sentence):
                    sentences += 1
                    word_index = 0
            line_fits.append((sentences, word_index))
        fits, word_index = 0, 0
        for r in range(rows):
            sentences, next_word_index = line_fits[word_index]
            fits += sentences
            word_index = next_word_index
        return fits
