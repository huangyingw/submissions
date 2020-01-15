class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = '0'
        while i >= 0 or j >= 0:
            ach = a[i] if i >= 0 else '0'
            bch = b[j] if j >= 0 else '0'
            if ach == bch:
                res.append(carry)
                carry = ach
            else:
                res.append('1' if carry == '0' else '0')
            i -= 1
            j -= 1
        if carry == '1':
            res.append(carry)
        return ''.join(res[::-1])

    def addBinary_integer(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            ach = int(a[i]) if i >= 0 else 0
            bch = int(b[j]) if j >= 0 else 0
            summ = ach + bch + carry
            res.append(str(summ % 2))
            carry = 1 if summ > 1 else 0
            i -= 1
            j -= 1
        if carry == 1:
            res.append(str(carry))
        return ''.join(res[::-1])

    def addBinary_xor(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            ach = ord(a[i]) - ord('0') if i >= 0 else 0
            bch = ord(b[j]) - ord('0') if j >= 0 else 0
            res.append(str(ach ^ bch ^ carry))
            carry = (ach + bch + carry) >> 1
            i -= 1
            j -= 1
        return ''.join(res[::-1])
