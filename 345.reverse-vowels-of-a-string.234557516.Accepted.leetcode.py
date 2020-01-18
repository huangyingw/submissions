class Solution(object):
    def reverseVowels(self, s):
        vowels = set(list('aeiouAEIOU'))
        string = list(s)
        l1, l2 = 0, len(string) - 1
        while l1 < l2:
            if string[l1] not in vowels:
                l1 += 1
            elif string[l2] not in vowels:
                l2 -= 1
            else:
                string[l1], string[l2] = string[l2], string[l1]
                l1 += 1
                l2 -= 1
        return "".join(string)
