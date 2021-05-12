class Solution(object):
    def maxLength(self, arr):
        char_sets = [set(s) for s in arr if len(s) == len(set(s))]
        dp = [set()]
        for char_set in char_sets:
            for prev_char_set in dp[:]:
                combo = char_set | prev_char_set
                if len(combo) == len(char_set) + len(prev_char_set):
                    dp.append(combo)
        return max(len(char_set) for char_set in dp)
