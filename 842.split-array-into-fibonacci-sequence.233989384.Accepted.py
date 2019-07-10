
















class Solution(object):
    def splitIntoFibonacci(self, S):

        MAX_NUM = 2 ** 31 - 1

        def helper(i, n1, n2):
            fib = [n1, n2]
            while i < len(S):
                next_num = fib[-1] + fib[-2]
                if next_num > MAX_NUM:
                    return []
                next_str = str(next_num)
                if S[i:i + len(next_str)] != next_str:
                    return []
                fib.append(next_num)
                i += len(next_str)
            return fib
        for len1 in range(1, (len(S) + 1) // 2):
            if len1 > 1 and S[0] == "0":
                return []
            n1 = int(S[:len1])
            if n1 > MAX_NUM:
                return []
            len2 = 1
            while len(S) - len1 - len2 >= max(len1, len2):
                if len2 > 1 and S[len1] == "0":
                    break
                n2 = int(S[len1:len1 + len2])
                if n2 > MAX_NUM:
                    break
                fibonacci = helper(len1 + len2, n1, n2)
                if fibonacci:
                    return fibonacci
                len2 += 1
        return []
