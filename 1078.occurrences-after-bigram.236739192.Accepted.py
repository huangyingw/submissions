


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        result = []
        if not text:
            return []
        splitted_text = text.split(' ')
        indi = 0
        for index in range(len(splitted_text) - 1):
            if splitted_text[index] == first and splitted_text[index + 1] == second:
                index = index + 2
                if index < len(splitted_text):
                    result.append(splitted_text[index])
        return result
