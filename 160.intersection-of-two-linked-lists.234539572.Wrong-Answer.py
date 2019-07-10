







class Solution(object):
    def getIntersectionNode(self, headA, headB):






        if not headA or not headB:
            return None
        p = headA
        q = headB
        while p and q:
            p = p.next
            q = q.next
        if p:

            temp = headA
            while p:
                p = p.next
                temp = temp.next
            p = headA
            q = headA
        elif q:

            temp = headB
            while q:
                q = q.next
                temp = temp.next
            p = headA
            q = temp
        else:

            p = headA
            q = headB
        while p != q:
            p = p.next
            q = q.next
        return p






        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa
