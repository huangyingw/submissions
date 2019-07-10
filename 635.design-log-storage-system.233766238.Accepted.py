

















class LogSystem(object):
    def __init__(self):
        self.prefixes = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}
        self.logs = []

    def put(self, id, timestamp):

        self.logs.append((id, timestamp))

    def retrieve(self, s, e, gra):

        result = []
        pref = self.prefixes[gra]
        s_prefix, e_prefix = s[:pref], e[:pref]
        for id, timestamp in self.logs:
            if s_prefix <= timestamp[:pref] <= e_prefix:
                result.append(id)
        return result



class LogNode(object):
    def __init__(self, nb_children):
        self.ids = set()
        self.children = [None for _ in range(nb_children)]


class LogSystem2(object):
    def __init__(self):
        self.periods = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
        self.nb_children = {"Year": 13, "Month": 32, "Day": 24, "Hour": 60, "Minute": 60, "Second": 0}
        self.root = LogNode(18)

    def put(self, id, timestamp):
        timelist = timestamp.split(":")
        timelist[0] = int(timelist[0]) - 2000
        node = self.root
        for t, period in zip(timelist, self.periods):
            if not node.children[int(t)]:
                node.children[int(t)] = LogNode(self.nb_children[period])
            node = node.children[int(t)]
            node.ids.add(id)

    def retrieve(self, s, e, gra):
        s_list, e_list = s.split(":"), e.split(":")
        s_list[0], e_list[0] = int(s_list[0]) - 2000, int(e_list[0]) - 2000
        s_node, e_node = self.root, self.root
        later, earlier = set(), set()
        for i in range(len(s_list)):
            s_val = int(s_list[i])
            s_child = s_node.children[s_val]
            for node in s_node.children[s_val + 1:]:
                if not node:
                    continue
                later |= node.ids
            if not s_child:
                break
            if gra == self.periods[i]:
                later |= s_child.ids
                break
            s_node = s_child
        for i in range(len(e_list)):
            e_val = int(e_list[i])
            e_child = e_node.children[e_val]
            for node in e_node.children[:e_val]:
                if not node:
                    continue
                earlier |= node.ids
            if not e_child:
                break
            if gra == self.periods[i]:
                earlier |= e_child.ids
                break
            e_node = e_child
        return list(earlier & later)
