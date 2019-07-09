_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """

        binary = bin(num)[2:][::-1]



        zero_highest = [1]
        one_highest = [1]
        if binary[0] == "0":
            count = 1
        else:
            count = 2
        for bit in range(1, len(binary)):

            zero_highest.append(zero_highest[-1] + one_highest[-1])

            one_highest.append(zero_highest[-2])
            if binary[bit] == "1" and binary[bit - 1] == "1":



                count = zero_highest[-1] + one_highest[-1]
            elif binary[bit] == "1" and binary[bit - 1] == "0":


                count += zero_highest[-1]


        return count
