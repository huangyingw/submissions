from collections import Counter


class Solution(object):
    def findMinStep(self, board, hand):
        def remove_sequences(board):
            start, end = 0, 0
            while end < len(board):
                if board[start] == board[end]:
                    end += 1
                elif end - start >= 3:
                    return remove_sequences(board[:start] + board[end:])
                else:
                    start = end
            if end - start >= 3:
                board = board[:start]
            return board

        def helper(board):
            if not board:
                return 0
            if not hand:
                return -1
            min_balls = 6
            start, end = 0, 0
            while end < len(board) + 1:
                if end == len(board) or board[start] != board[end]:
                    need = 3 - (end - start)
                    colour = board[start]
                    if hand[colour] >= need:
                        hand[colour] -= need
                        next_board = remove_sequences(board[:start] + board[end:])
                        min_end = helper(next_board)
                        if min_end != -1:
                            min_balls = min(need + min_end, min_balls)
                        hand[colour] += need
                    start = end
                end += 1
            return -1 if min_balls == 6 else min_balls
        hand = Counter(hand)
        return helper(board)
