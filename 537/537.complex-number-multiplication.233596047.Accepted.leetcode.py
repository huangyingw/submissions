class Solution(object):
    def complexNumberMultiply(self, a, b):
        a_real, a_im = a.split("+")
        a_real, a_im = int(a_real), int(a_im[:-1])
        b_real, b_im = b.split("+")
        b_real, b_im = int(b_real), int(b_im[:-1])
        c_real = a_real * b_real - a_im * b_im
        c_im = a_real * b_im + a_im * b_real
        return str(c_real) + "+" + str(c_im) + "i"
