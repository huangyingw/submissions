_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def minWindow(self, S, T):

        next_in_s = [None for _ in range(len(S))]
        next_by_letter = [-1 for _ in range(26)]
        for i in range(len(S) - 1, -1, -1):
            next_in_s[i] = next_by_letter[:]
            next_by_letter[ord(S[i]) - ord("a")] = i


        matches = [[i, i] for i, c in enumerate(S) if c == T[0]]
        if not matches:
            return ""
        for i, c in enumerate(T[1:], 1):
            new_matches = []
            for s_start, s_last in matches:
                s_next = next_in_s[s_last][ord(c) - ord("a")]
                if s_next != -1:
                    new_matches.append([s_start, s_next])
            if not new_matches:
                return ""
            matches = new_matches

        start, end = min(matches, key=lambda i, j: j - i)
        return S[start:end + 1]
