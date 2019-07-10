_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def numComponents(self, head, G):

        H = set(G)
        count = 0
        connected = False
        while head:
            if head.val in H and not connected:
                connected = True
                count += 1
            elif head.val not in G and connected:
                connected = False
            head = head.next
        return count
