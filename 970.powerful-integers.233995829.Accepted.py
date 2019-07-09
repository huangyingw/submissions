_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()

        def make_power_list(val):
            power_list = [1]
            if val != 1:
                while power_list[-1] <= bound:
                    power_list.append(power_list[-1] * val)
                power_list.pop()
            return power_list
        x_list, y_list = make_power_list(x), make_power_list(y)
        for x_num in x_list:
            for y_num in y_list:
                if x_num + y_num > bound:
                    break
                result.add(x_num + y_num)
        return list(result)
