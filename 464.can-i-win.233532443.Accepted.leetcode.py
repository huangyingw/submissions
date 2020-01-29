class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        return self.next_player_win(desiredTotal, list(range(1, maxChoosableInteger + 1)), {})

    def next_player_win(self, target, unused, memo):
        if unused[-1] >= target:
            return True
        tup = tuple(unused)
        if tup in memo:
            return memo[tup]
        for i in range(len(unused) - 1, -1, -1):
            opposition_win = self.next_player_win(target - unused[i], unused[:i] + unused[i + 1:], memo)
            if not opposition_win:
                memo[tup] = True
                return True
        memo[tup] = False
        return False
