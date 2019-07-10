class Solution:
    def mostCommonWord(self, paragraph, banned):
        for c in string.punctuation:
            paragraph = paragraph.replace(c, "")
        paragraph = paragraph.lower()
        nparagraph = paragraph.split()
        nparagraph = [x for x in nparagraph if x not in banned]
        temp = collections.Counter(nparagraph)
        return max(temp.items(), key=operator.itemgetter(1))[0]
