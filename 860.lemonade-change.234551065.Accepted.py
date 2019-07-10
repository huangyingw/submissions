class Solution(object):
    def lemonadeChange(self, bills):
        fives = tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if not fives:
                    return False
                tens += 1
                fives -= 1
            else:
                if fives and tens:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
