class Solution:
    def findRestaurant(self, list1, list2):
        common = set(list1) & set(list2)
        index_sum = 0
        res = []
        for i in common:
            index_sum = list1.index(i) + list2.index(i)
            res.append((index_sum, list1.index(i)))
        res.sort()
        ret = []
        sum_index = res[0][0]
        for i in res:
            if i[0] == sum_index:
                ret.append(list1[i[1]])
        return ret

    def findRestaurant(self, list1, list2):
        d = {}
        for i, r in enumerate(list1):
            d[r] = i
        res = []
        imin = len(list1) + len(list2)
        for i, r in enumerate(list2):
            if r in d and d[r] + i <= imin:
                if d[r] + i == imin:
                    res.append(r)
                else:
                    res = []
                    res.append(r)
                    imin = d[r] + i
        return res
