class Solution(object):
    def gcdOfStrings(self, str1, str2):

        if len(str1) > len(str2):
            str1, str2 = str2, str1
        l_str1 = len(str1)
        for index in range(1, len(str1) + 1):
            if l_str1 % index != 0:
                continue
            size_to_take = int(l_str1 / index)
            substr1 = str1[:size_to_take]
            substr2 = str2
            while substr1 == substr2[:size_to_take]:
                substr2 = substr2[size_to_take:]
            if substr2 == "":
                return substr1
        return ""
