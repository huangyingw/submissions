
class Solution:

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


    def toLowerCase2(self, str):
        result = ""
        for c in str:
            if c >= "A" and c <= "Z":
                result = result + chr(ord(c) + 32)
            else:
                result = result + c
        return result
