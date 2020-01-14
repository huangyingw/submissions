from collections import OrderedDict
class Solution(object):
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        running_sum = 0
        sum_to_node = OrderedDict()
        while node:
            running_sum += node.val
            to_connect = sum_to_node.get(running_sum, node)
            while running_sum in sum_to_node:
                sum_to_node.popitem()
            sum_to_node[running_sum] = to_connect
            node = to_connect.next = node.next
        return dummy.next
