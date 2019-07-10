class Solution(object):
    def numTilePossibilities(self, tiles):

        if not tiles:
            return 0
        import collections
        unique = set(tiles)
        freq_map = collections.Counter(tiles)
        total_len = 1
        while total_len < len(tiles):
            new = set()
            for char in tiles:
                for comb in unique:
                    new_seq = comb + char
                    up_freq = collections.Counter(new_seq)
                    flag = True
                    for key, val in up_freq.items():
                        if val > freq_map[key]:
                            flag = False
                    if flag:
                        new.add(new_seq)

            unique.update(new)
            total_len += 1
        return len(unique)
