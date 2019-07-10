import gc


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        savedA, savedB = headA, headB
        while headA != headB:
            headA = savedB if not headA else headA.next
            headB = savedA if not headB else headB.next
        gc.collect()
        return headA


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        savedA, savedB = headA, headB
        len_diff = 0
        while headA.next:
            len_diff += 1
            headA = headA.next
        while headB.next:
            len_diff -= 1
            headB = headB.next
        if headA != headB:
            return
        headA, headB = savedA, savedB
        while len_diff != 0:
            if len_diff > 0:
                headA = headA.next
                len_diff -= 1
            else:
                headB = headB.next
                len_diff += 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        gc.collect()
        return headA
