class Solution:
    def reverseBits(self, n):
        binary = bin(n)
        binary = binary[2:]
        reversed_binary = binary[::-1] + ''.join(['0' for _ in range(32 - len(binary))])
        return int(reversed_binary, 2)
class Solution2:
    def reverseBits(self, n):
        reversed, bit = 0, 31
        while n != 0:
            if n % 2 == 1:
                reversed += 2**bit
            bit -= 1
            n //= 2
        return reversed
