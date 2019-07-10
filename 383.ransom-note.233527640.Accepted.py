








from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        mag_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        for c in ransom_count:
            if c not in mag_count or mag_count[c] < ransom_count[c]:
                return False
        return True
