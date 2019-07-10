


class Solution(object):
    def flipAndInvertImage(self, A):

        for row in A:
            for i in xrange((len(row) + 1) / 2):

                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
