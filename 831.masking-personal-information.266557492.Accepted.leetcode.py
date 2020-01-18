class Solution(object):
    def maskPII(self, S):
        if '@' in S:
            S = S.lower()
            firstChar = S[0]
            asterix = S.find('@')
            return S[0] + "*****" + S[asterix - 1:]
        else:
            S = S.replace('+', "")
            S = S.replace('(', '')
            S = S.replace('-', '')
            S = S.replace(')', '')
            S = S.replace(' ', '')
            if len(S) == 10:
                return "***-***-" + S[-4:]
            else:
                countryCode = len(S) - 10
                result = "+"
                for index in range(countryCode):
                    result += "*"
                return result + "-***-***-" + S[-4:]
