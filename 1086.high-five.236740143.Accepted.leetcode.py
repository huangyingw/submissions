class Solution(object):
    def highFive(self, items):
        if not items:
            return []
        score_map = {}
        for item in items:
            if item[0] in score_map:
                score_map[item[0]].append(item[1])
            else:
                score_map[item[0]] = [item[1]]
        result = []
        for key, value in score_map.items():
            value.sort(reverse=True)
            if len(value) >= 5:
                average = value[:5]
            else:
                average = value
            score_map[key] = sum(average) / len(average)
            result.append([key, score_map[key]])
        return result
