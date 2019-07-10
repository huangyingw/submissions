














class Solution(object):
    def largestOverlap(self, A, B):

        def image_to_bits(image):
            bits = []
            for row in image:
                num = 0
                for i, bit in enumerate(reversed(row)):
                    if bit == 1:
                        num += (bit << i)
                bits.append(num)
            return bits
        A_bits, B_bits = image_to_bits(A), image_to_bits(B)
        rows, cols = len(A), len(A[0])
        max_overlap = 0
        for slide, static in ((A_bits, B_bits), (B_bits, A_bits)):
            for row_shift in range(rows):
                for col_shift in range(cols):
                    overlap = 0
                    for slide_row in range(rows - row_shift):
                        shifted = slide[slide_row] >> col_shift
                        row_and = bin(shifted & static[slide_row + row_shift])
                        overlap += row_and.count("1")
                    max_overlap = max(max_overlap, overlap)
        return max_overlap
