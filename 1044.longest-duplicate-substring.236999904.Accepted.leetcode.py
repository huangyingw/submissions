class Solution(object):
    def longestDupSubstring(self, S):
        MOD = 2 ** 63 - 1
        MULTIPLIER = 26
        s = [ord(c) - ord("a") for c in S]

        def test(guess):
            hash_value = 0
            for i in range(guess):
                hash_value = (hash_value * MULTIPLIER + s[i]) % MOD
            val = (MULTIPLIER ** guess) % MOD
            seen = {hash_value}
            for i in range(guess, len(S)):
                hash_value = (hash_value * MULTIPLIER + s[i] - s[i - guess] * val) % MOD
                if hash_value in seen:
                    return i - guess + 1
                seen.add(hash_value)
        result, low, high = 0, 0, len(S)
        while low < high:
            mid = (low + high + 1) / 2
            index = test(mid)
            if index:
                low = mid
                result = index
            else:
                high = mid - 1
        return S[result:result + low]
