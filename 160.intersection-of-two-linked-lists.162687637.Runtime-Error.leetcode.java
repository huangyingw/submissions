public class Solution
{
    public ListNode getIntersectionNode(ListNode headA, ListNode headB)
    {
        if (headA == null || headB == null)
        {
            return null;
        }

        ListNode pA = headA;
        ListNode pB = headB;
        ListNode tailA = null;
        ListNode tailB = null;

        while (true)
        {
            if (pA == null)
            {
                pA = headB;
            }
            else if (pB == null)
            {
                pB = headA;
            }
            else if (pA.next == null)
            {
                tailA = pA;
            }
            else if (pB.next == null)
            {
                tailB = pB;
            }
            else if (tailA != null && tailB != null && tailA != tailB)
            {
                return null;
            }
            else if (pA == pB)
            {
                return pA;
            }

            pA = pA.next;
            pB = pB.next;
        }
    }

}
