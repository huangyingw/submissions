











class Solution(object):
    def sequenceReconstruction(self, org, seqs):

        extended = [None] + org
        pairs = set((n1, n2) for n1, n2 in zip(extended, org))
        num_to_index = {num: i for i, num in enumerate(extended)}
        for seq in seqs:
            for n1, n2 in zip([None] + seq, seq):
                if n2 not in num_to_index or num_to_index[n2] <= num_to_index[n1]:
                    return False
                last_index = num_to_index[n2]
                pairs.discard((n1, n2))
        return not pairs
