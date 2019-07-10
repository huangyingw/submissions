class Solution(object):
    def equationsPossible(self, equations):

        equal_list, unequal_list = [], []
        for equation in equations:
            x, y = equation[0], equation[3]
            if '==' in equation:
                if not equal_list:
                    equal_list.append(x + y)
                else:
                    found = False
                    for index in range(0, len(equal_list)):
                        val = equal_list[index]
                        if x in val or y in val:
                            val = val + x + y
                            equal_list[index] = val
                            found = True
                    if not found:
                        equal_list.append(x + y)
            else:
                if x == y:
                    return False
                unequal_list.append([x, y])
        for val in unequal_list:
            for equal in equal_list:
                if val[0] in equal and val[1] in equal:
                    return False
        return True
