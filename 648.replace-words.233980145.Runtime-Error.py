class Solution(object):
    def replaceWords(self, dict, sentence):
        result = []
        root = {}
        for word in dict:
            node = root
            for c in word[:-1]:
                if c not in node:
                    node[c] = {}
                elif isinstance(node[c], str):
                    break
                node = node[c]
            else:
                node[word[-1]] = word
        sentence = sentence.split(" ")
        for word in sentence:
            node = root
            for c in word:
                if c not in node:
                    result.append(word)
                    break
                if isinstance(node[c], str):
                    result.append(node[c])
                    break
                node = node[c]
            else:
                result.append(word)
        return " ".join(result)
