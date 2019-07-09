_author_ = 'jake'
_project_ = 'leetcode'















import heapq
from collections import defaultdict


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target_set, remaining_target = set(target), set(target)
        char_to_word = defaultdict(set)
        for sticker in stickers:
            cleaned = tuple(x for x in sticker if x in target_set)
            sticker_set = set(cleaned)
            for c in sticker_set:
                char_to_word[c].add(cleaned)
            remaining_target -= sticker_set
        if remaining_target:
            return -1
        heap = [(0, len(target), list(target))]
        while True:
            used_words, target_len, target_str = heapq.heappop(heap)
            for sticker in char_to_word[target_str[0]]:
                new_str = target_str[:]
                for ch in sticker:
                    if ch in new_str:
                        new_str.remove(ch)
                if not new_str:
                    return used_words + 1
                heapq.heappush(heap, (used_words + 1, len(new_str), new_str))
