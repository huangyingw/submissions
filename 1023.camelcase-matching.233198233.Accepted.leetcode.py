class Solution(object):
    def camelMatch(self, queries, pattern):
        import re
        result = []
        patterns = re.findall('[A-Z][a-z]*', pattern)
        for query in queries:
            splitter = re.findall('[A-Z][a-z]*', query)
            flag = True
            if len(patterns) == len(splitter):
                for index in range(len(patterns)):
                    p_i, s_i = 1, 1
                    if patterns[index][0] == splitter[index][0]:
                        while p_i < len(patterns[index]) and s_i < len(splitter[index]):
                            if patterns[index][p_i] == splitter[index][s_i]:
                                p_i += 1
                                s_i += 1
                            else:
                                s_i += 1
                        if p_i != len(patterns[index]):
                            flag = False
                            break
                    else:
                        flag = False
                        break
                if flag:
                    result.append(True)
                else:
                    result.append(False)
            else:
                result.append(False)
        return result
