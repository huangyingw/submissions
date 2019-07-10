











class Solution(object):
    def slidingPuzzle(self, board):

        nbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def next_boards(b):
            i = b.index(0)
            next_bds = []
            for nbor in nbors[i]:
                b_copy = b[:]
                b_copy[i], b_copy[nbor] = b_copy[nbor], b_copy[i]
                next_bds.append(b_copy)
            return next_bds
        queue = [board[0] + board[1]]
        steps = 0
        seen = set()
        while queue:
            new_queue = []
            for bd in queue:
                if bd == [1, 2, 3, 4, 5, 0]:
                    return steps
                seen.add(tuple(bd))
                new_queue += [nb for nb in next_boards(bd) if tuple(nb) not in seen]
            steps += 1
            queue = new_queue
        return -1
