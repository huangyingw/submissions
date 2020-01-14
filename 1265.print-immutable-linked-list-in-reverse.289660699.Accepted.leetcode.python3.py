class Solution(object):
    if not head.getNext():
        return
class Solution2(object):
    node = head
    length = 0
    while node:
        length += 1
        node = node.getNext()
    for i in range(length - 1, -1, -1):
        node = head
        for _ in range(i):
            node = node.getNext()
class Solution3(object):
    node = head
    length = 0
    while node:
        length += 1
        node = node.getNext()
    interval = int(length ** 0.5)
    node = head
    counter = 0
    partition_nodes = []
    while node:
        if counter % interval == 0:
            partition_nodes.append(node)
        counter += 1
        node = node.getNext()
    for i in range(len(partition_nodes) - 1, -1, -1):
        node = partition_nodes[i]
        interval_end = partition_nodes[i + 1] if i != len(partition_nodes) - 1 else None
        interval_nodes = []
        while node != interval_end:
            interval_nodes.append(node)
            node = node.getNext()
        for print_node in interval_nodes[::-1]:
