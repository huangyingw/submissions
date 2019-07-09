






class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa if pa else None
