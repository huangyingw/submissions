_author_ = 'jake'
_project_ = 'leetcode'
# You are given an immutable linked list,
# ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
# You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):
# ImmutableListNode.getNext(): Return the next node.
# The input is only given to initialize the linked list internally.
# You must solve this problem without modifying the linked list.
# In other words, you must operate the linked list using only the mentioned APIs.
# Else recurse for the next node, printing it out after the recursion returns.
# Time - O(n)
# Space - O(n), call stack of n functions.
# Alternatively, find the length of the list and iterate to each node in reverse order,
# which is O(n**2) time but O(1) space.
# Alternatively, divide the list into intervals of length sqrt(n).
# Make a list of nodes at the start of each interval.
# This is O(n) time and O(sqrt(n)) space.


class Solution(object):
    """
    :type head: ImmutableListNode
    :rtype: None
    """
    if not head.getNext():
        return


class Solution2(object):
    node = head
    length = 0
    while node:
        length += 1
        node = node.getNext()
    for i in range(length - 1, -1, -1):     # get each value in reverse order
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
    partition_nodes = []            # nodes at start of each interval
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
