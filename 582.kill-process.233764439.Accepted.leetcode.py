from collections import defaultdict
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        node_to_children = defaultdict(list)
        for node, parent in zip(pid, ppid):
            node_to_children[parent].append(node)
        killed, to_kill = [], [kill]
        while to_kill:
            process = to_kill.pop()
            killed.append(process)
            to_kill += node_to_children[process]
        return killed
